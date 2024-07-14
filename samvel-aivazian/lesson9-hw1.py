import json
from typing import List, Protocol


class Recipe:
    def __init__(self, title: str, ingredients: List[str], instructions: str, special_diet: bool = False) -> None:
        self.title: str = title
        self.ingredients: List[str] = ingredients
        self.instructions: str = instructions
        self.special_diet: bool = special_diet

    def __str__(self) -> str:
        return (f"Title: {self.title}, Ingredients: {', '.join(self.ingredients)}, Instructions: {self.instructions}, "
                f"Special Diet: {self.special_diet}")


class RecipeStorage(Protocol):
    def save(self, recipes: List[Recipe]) -> None:
        ...

    def load(self) -> List[Recipe]:
        ...


class FileStorage:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def save(self, recipes: List[Recipe]) -> None:
        with open(self.filename, 'w') as file:
            json.dump([recipe.__dict__ for recipe in recipes], file, indent=4)

    def load(self) -> List[Recipe]:
        try:
            with open(self.filename, 'r') as file:
                recipes_data = json.load(file)
                return [Recipe(**data) for data in recipes_data]
        except FileNotFoundError:
            return []


class RecipeManager:
    def __init__(self, storage: RecipeStorage) -> None:
        self.storage: RecipeStorage = storage
        self.recipes: List[Recipe] = self.storage.load()

    def add_recipe(self, recipe: Recipe) -> None:
        self.recipes.append(recipe)
        self.storage.save(self.recipes)

    def remove_recipe(self, title: str) -> None:
        self.recipes = [recipe for recipe in self.recipes if recipe.title != title]
        self.storage.save(self.recipes)

    def update_recipe(self, title: str, updated_recipe: Recipe) -> None:
        self.recipes = [updated_recipe if recipe.title == title else recipe for recipe in self.recipes]
        self.storage.save(self.recipes)

    def list_recipes(self) -> None:
        for recipe in self.recipes:
            self.display_recipe(recipe)

    def search_recipes_by_ingredient(self, ingredient: str) -> List[Recipe]:
        return [recipe for recipe in self.recipes if ingredient in recipe.ingredients]

    def display_recipe(self, recipe: Recipe) -> None:
        print(recipe)


def main() -> None:
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
