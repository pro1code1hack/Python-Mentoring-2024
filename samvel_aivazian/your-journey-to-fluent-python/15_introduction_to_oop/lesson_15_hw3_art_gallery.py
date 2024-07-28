import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')


def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
        return result

    return wrapper


class Artist:
    def __init__(self, name):
        self.name = name
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)


class Artwork:
    def __init__(self, title, price, artist):
        self.title = title
        self.price = price
        self.artist = artist
        artist.add_artwork(self)


class Gallery:
    def __init__(self):
        self.artworks = []
        self.sales = 0

    @execution_time_decorator
    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        logging.info(f"Artwork added: {artwork.title} by {artwork.artist.name}")

    @execution_time_decorator
    def sell_artwork(self, title):
        for artwork in self.artworks:
            if artwork.title == title:
                self.artworks.remove(artwork)
                self.sales += artwork.price
                logging.info(f"Sold artwork: {title} for ${artwork.price}")
                return
        logging.info("Artwork not found.")

    @execution_time_decorator
    def display_artworks(self):
        if not self.artworks:
            logging.info("No artworks available.")
        for artwork in self.artworks:
            logging.info(f"Artwork: {artwork.title} by {artwork.artist.name} - ${artwork.price}")

    @execution_time_decorator
    def total_sales(self):
        logging.info(f"Total sales: ${self.sales}")


if __name__ == "__main__":
    gallery = Gallery()

    artist1 = Artist("Vincent van Gogh")
    artist2 = Artist("Pablo Picasso")

    artwork1 = Artwork("Starry Night", 1000000, artist1)
    artwork2 = Artwork("The Weeping Woman", 2000000, artist2)

    gallery.add_artwork(artwork1)
    gallery.add_artwork(artwork2)

    gallery.display_artworks()
    gallery.sell_artwork("Starry Night")
    gallery.display_artworks()
    gallery.total_sales()
