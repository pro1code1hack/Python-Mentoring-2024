from typing import List


class Artist:
    """
    A class to represent an artist.

    Attributes:
    name (str): The name of the artist.
    bio (str): A brief biography of the artist.
    """

    def __init__(self, name: str, bio: str) -> None:
        self.name: str = name
        self.bio: str = bio


class Artwork:
    """
    A class to represent an artwork.

    Attributes:
    title (str): The title of the artwork.
    artist (Artist): The artist who created the artwork.
    price (float): The price of the artwork.
    """

    def __init__(self, title: str, artist: Artist, price: float) -> None:
        self.title: str = title
        self.artist: Artist = artist
        self.price: float = price

    def display_details(self) -> None:
        """
        Display the details of the artwork.
        """
        print(f"Title: {self.title}, Artist: {self.artist.name}, Price: ${self.price}")


class Painting(Artwork):
    """
    A class to represent a painting, inheriting from Artwork.

    Attributes:
    medium (str): The medium used in the painting.
    """

    def __init__(self, title: str, artist: Artist, price: float, medium: str) -> None:
        super().__init__(title, artist, price)
        self.medium: str = medium

    def display_details(self) -> None:
        """
        Display the details of the painting, including the medium.
        """
        super().display_details()
        print(f"Medium: {self.medium}")


class Sculpture(Artwork):
    """
    A class to represent a sculpture, inheriting from Artwork.

    Attributes:
    material (str): The material used in the sculpture.
    """

    def __init__(self, title: str, artist: Artist, price: float, material: str) -> None:
        super().__init__(title, artist, price)
        self.material: str = material

    def display_details(self) -> None:
        """
        Display the details of the sculpture, including the material.
        """
        super().display_details()
        print(f"Material: {self.material}")


class Gallery:
    """
    A class to represent an art gallery.

    Attributes:
    artworks (List[Artwork]): A list of artworks in the gallery.
    sales (float): The total sales made by the gallery.
    """

    def __init__(self) -> None:
        self.artworks: List[Artwork] = []
        self.sales: float = 0.0

    def add_artwork(self, artwork: Artwork) -> None:
        """
        Add an artwork to the gallery.

        Args:
        artwork (Artwork): The artwork to add.
        """
        self.artworks.append(artwork)

    def sell_artwork(self, title: str) -> None:
        """
        Sell an artwork by its title.

        Args:
        title (str): The title of the artwork to sell.
        """
        for artwork in self.artworks:
            if artwork.title == title:
                self.artworks.remove(artwork)
                self.sales += artwork.price
                print(f"Artwork '{title}' sold for ${artwork.price}.")
                return
        print(f"Artwork '{title}' not found.")

    def display_artworks(self) -> None:
        """
        Display all artworks currently in the gallery.
        """
        if not self.artworks:
            print("No artworks in the gallery.")
        for artwork in self.artworks:
            artwork.display_details()

    def display_sales(self) -> None:
        """
        Display the total sales made by the gallery.
        """
        print(f"Total sales: ${self.sales}")


def main() -> None:
    """
    Main function to run the gallery simulation.
    """
    gallery = Gallery()

    artist1 = Artist("Vincent van Gogh", "A Dutch post-impressionist painter.")
    artist2 = Artist("Pablo Picasso", "A Spanish painter, sculptor, print maker, ceramicist, and stage designer.")
    artist3 = Artist("Van Darkholme", "A semen arsonist from the dungeon")

    painting = Painting("Starry Night", artist1, 1000000.0, "Oil on canvas")
    sculpture = Sculpture("The Thinker", artist2, 1500000.0, "Bronze")
    masterpiece = Painting("Masterpiece #1", artist3, 300, "Lube on semen")

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
