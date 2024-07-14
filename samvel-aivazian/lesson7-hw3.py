from typing import List


class Artist:
    def __init__(self, name: str, bio: str) -> None:
        self.name: str = name
        self.bio: str = bio


class Artwork:
    def __init__(self, title: str, artist: Artist, price: float) -> None:
        self.title: str = title
        self.artist: Artist = artist
        self.price: float = price

    def display_details(self) -> None:
        print(f"Title: {self.title}, Artist: {self.artist.name}, Price: ${self.price}")


class Painting(Artwork):
    def __init__(self, title: str, artist: Artist, price: float, medium: str) -> None:
        super().__init__(title, artist, price)
        self.medium: str = medium

    def display_details(self) -> None:
        super().display_details()
        print(f"Medium: {self.medium}")


class Sculpture(Artwork):
    def __init__(self, title: str, artist: Artist, price: float, material: str) -> None:
        super().__init__(title, artist, price)
        self.material: str = material

    def display_details(self) -> None:
        super().display_details()
        print(f"Material: {self.material}")


class Gallery:
    def __init__(self) -> None:
        self.artworks: List[Artwork] = []
        self.sales: float = 0.0

    def add_artwork(self, artwork: Artwork) -> None:
        self.artworks.append(artwork)

    def sell_artwork(self, title: str) -> None:
        for artwork in self.artworks:
            if artwork.title == title:
                self.artworks.remove(artwork)
                self.sales += artwork.price
                print(f"Artwork '{title}' sold for ${artwork.price}.")
                return
        print(f"Artwork '{title}' not found.")

    def display_artworks(self) -> None:
        if not self.artworks:
            print("No artworks in the gallery.")
        for artwork in self.artworks:
            artwork.display_details()

    def display_sales(self) -> None:
        print(f"Total sales: ${self.sales}")


def main() -> None:
    gallery: Gallery = Gallery()

    artist1: Artist = Artist("Vincent van Gogh", "A Dutch post-impressionist painter.")
    artist2: Artist = Artist("Pablo Picasso",
                             "A Spanish painter, sculptor, print maker, ceramicist, and stage designer.")
    artist3: Artist = Artist("Van Darkholme", "A semen arsonist from the dungeon")

    painting: Painting = Painting("Starry Night", artist1, 1000000.0, "Oil on canvas")
    sculpture: Sculpture = Sculpture("The Thinker", artist2, 1500000.0, "Bronze")
    masterpiece: Painting = Painting("Masterpiece #1", artist3, 300, "Lube on semen")

    gallery.add_artwork(painting)
    gallery.add_artwork(sculpture)
    gallery.add_artwork(masterpiece)

    print("Artworks in the gallery:")
    gallery.display_artworks()

    gallery.sell_artwork("Starry Night")

    print("\nRemaining artworks in the gallery:")
    gallery.display_artworks()
    gallery.display_sales()


if __name__ == "__main__":
    main()
