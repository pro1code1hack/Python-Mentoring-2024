import json
from typing import List, Protocol


class Recipe:
    """
    A class to represent a recipe.

    Attributes:
    title (str): The title of the recipe.
    ingredients (List[str]): A list of ingredients for the recipe.
    instructions (str): The instructions to prepare the recipe.
    special_diet (bool): Indicates if the recipe is for a special diet.
    """

    def __init__(self, title: str, ingredients: List[str], instructions: str, special_diet: bool = False) -> None:
        self.title: str = title
        self.ingredients: List[str] = ingredients
        self.instructions: str = instructions
        self.special_diet: bool = special_diet

    def __str__(self) -> str:
        return (f"Title: {self.title}, Ingredients: {', '.join(self.ingredients)}, Instructions: {self.instructions}, "
                f"Special Diet: {self.special_diet}")


class RecipeStorage(Protocol):
    """
    A protocol for recipe storage classes.
    """

    def save(self, recipes: List[Recipe]) -> None:
        ...

    def load(self) -> List[Recipe]:
        ...


class FileStorage:
    """
    A class to handle file storage for recipes using JSON.

    Attributes:
    filename (str): The name of the file to store recipes.
    """

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def save(self, recipes: List[Recipe]) -> None:
        """
        Save the list of recipes to a file.

        Args:
        recipes (List[Recipe]): The list of recipes to save.
        """
        with open(self.filename, 'w') as file:
            json.dump([recipe.__dict__ for recipe in recipes], file, indent=4)

    def load(self) -> List[Recipe]:
        """
        Load the list of recipes from a file.

        Returns:
        List[Recipe]: The list of loaded recipes.
        """
        try:
            with open(self.filename, 'r') as file:
                recipes_data = json.load(file)
                return [Recipe(**data) for data in recipes_data]
        except FileNotFoundError:
            return []


class RecipeManager:
    """
    A class to manage recipes.

    Attributes:
    storage (RecipeStorage): The storage backend for recipes.
    recipes (List[Recipe]): The list of recipes.
    """

    def __init__(self, storage: RecipeStorage) -> None:
        self.storage: RecipeStorage = storage
        self.recipes: List[Recipe] = self.storage.load()

    def add_recipe(self, recipe: Recipe) -> None:
        """
        Add a new recipe to the manager.

        Args:
        recipe (Recipe): The recipe to add.
        """
        self.recipes.append(recipe)
        self.storage.save(self.recipes)

    def remove_recipe(self, title: str) -> None:
        """
        Remove a recipe by its title.

        Args:
        title (str): The title of the recipe to remove.
        """
        self.recipes = [recipe for recipe in self.recipes if recipe.title != title]
        self.storage.save(self.recipes)

    def update_recipe(self, title: str, updated_recipe: Recipe) -> None:
        """
        Update an existing recipe by its title.

        Args:
        title (str): The title of the recipe to update.
        updated_recipe (Recipe): The updated recipe.
        """
        self.recipes = [updated_recipe if recipe.title == title else recipe for recipe in self.recipes]
        self.storage.save(self.recipes)

    def list_recipes(self) -> None:
        """
        List all recipes.
        """
        for recipe in self.recipes:
            self.display_recipe(recipe)

    def search_recipes_by_ingredient(self, ingredient: str) -> List[Recipe]:
        """
        Search for recipes that contain a specific ingredient.

        Args:
        ingredient (str): The ingredient to search for.

        Returns:
        List[Recipe]: The list of recipes containing the ingredient.
        """
        return [recipe for recipe in self.recipes if ingredient in recipe.ingredients]

    def display_recipe(self, recipe: Recipe) -> None:
        """
        Display the details of a recipe.

        Args:
        recipe (Recipe): The recipe to display.
        """
        print(recipe)


def main() -> None:
    """
    Main function to demonstrate the functionality of the RecipeManager.
    """
    storage = FileStorage("recipes.json")
    manager = RecipeManager(storage)

    # Add a new recipe
    pasta_recipe = Recipe("Pasta", ["Pasta", "Tomato", "Basil"],
                          "Boil pasta, add tomato sauce", special_diet=False)
    manager.add_recipe(pasta_recipe)

    # List all recipes
    print("All recipes:")
    manager.list_recipes()

    # Search recipes by ingredient
    ingredient_to_search = "Tomato"
    print(f"\nRecipes with ingredient '{ingredient_to_search}':")
    recipes_with_tomato = manager.search_recipes_by_ingredient(ingredient_to_search)
    for recipe in recipes_with_tomato:
        manager.display_recipe(recipe)

    # Update a recipe
    updated_pasta_recipe = Recipe("Pasta", ["Pasta", "Tomato", "Basil", "Garlic"],
                                  "Boil pasta, add tomato sauce and garlic", special_diet=False)
    manager.update_recipe("Pasta", updated_pasta_recipe)

    # List all recipes after update
    print("\nAll recipes after update:")
    manager.list_recipes()

    # Remove a recipe
    manager.remove_recipe("Pasta")

    # List all recipes after removal
    print("\nAll recipes after removal:")
    manager.list_recipes()


if __name__ == "__main__":
    main()
