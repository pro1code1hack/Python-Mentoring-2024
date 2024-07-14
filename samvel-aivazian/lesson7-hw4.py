from typing import List, Tuple


class Ingredient:
    """
    A class to represent an ingredient.

    Attributes:
    name (str): The name of the ingredient.
    quantity (str): The quantity of the ingredient.
    """

    def __init__(self, name: str, quantity: str) -> None:
        self.name: str = name
        self.quantity: str = quantity


class Recipe:
    """
    A class to represent a recipe.

    Attributes:
    name (str): The name of the recipe.
    ingredients (List[Ingredient]): A list of ingredients required for the recipe.
    instructions (str): The instructions to prepare the recipe.
    """

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.ingredients: List[Ingredient] = []
        self.instructions: str = ""

    def add_ingredient(self, ingredient: Ingredient) -> None:
        """
        Add an ingredient to the recipe.

        Args:
        ingredient (Ingredient): The ingredient to add.
        """
        self.ingredients.append(ingredient)

    def set_instructions(self, instructions: str) -> None:
        """
        Set the instructions for the recipe.

        Args:
        instructions (str): The instructions to set.
        """
        self.instructions = instructions

    def display(self) -> None:
        """
        Display the recipe details, including its ingredients and instructions.
        """
        print(f"Recipe: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"{ingredient.name}: {ingredient.quantity}")
        print("Instructions:")
        print(self.instructions)


class Cookbook:
    """
    A class to represent a cookbook.

    Attributes:
    recipes (List[Recipe]): A list of recipes in the cookbook.
    """

    def __init__(self) -> None:
        self.recipes: List[Recipe] = []

    def add_recipe(self, recipe: Recipe) -> None:
        """
        Add a recipe to the cookbook.

        Args:
        recipe (Recipe): The recipe to add.
        """
        self.recipes.append(recipe)

    def find_recipes_by_ingredient(self, ingredient_name: str) -> List[Recipe]:
        """
        Find recipes that contain a specific ingredient.

        Args:
        ingredient_name (str): The name of the ingredient to search for.

        Returns:
        List[Recipe]: A list of recipes that contain the ingredient.
        """
        found_recipes = []
        for recipe in self.recipes:
            for ingredient in recipe.ingredients:
                if ingredient.name.lower() == ingredient_name.lower():
                    found_recipes.append(recipe)
                    break
        return found_recipes

    def display_all_recipes(self) -> None:
        """
        Display all recipes in the cookbook.
        """
        if not self.recipes:
            print("No recipes in the cookbook.")
        else:
            for recipe in self.recipes:
                recipe.display()


class IngredientFactory:
    """
    A factory class for creating Ingredient objects.
    """

    @staticmethod
    def create_ingredient(name: str, quantity: str) -> Ingredient:
        """
        Create an Ingredient object.

        Args:
        name (str): The name of the ingredient.
        quantity (str): The quantity of the ingredient.

        Returns:
        Ingredient: The created Ingredient object.
        """
        return Ingredient(name, quantity)


class RecipeFactory:
    """
    A factory class for creating Recipe objects.
    """

    @staticmethod
    def create_recipe(name: str, ingredients: List[Tuple[str, str]], instructions: str) -> Recipe:
        """
        Create a Recipe object.

        Args:
        name (str): The name of the recipe.
        ingredients (List[Tuple[str, str]]): A list of ingredient name and quantity tuples.
        instructions (str): The instructions for the recipe.

        Returns:
        Recipe: The created Recipe object.
        """
        recipe = Recipe(name)
        for ingredient_name, quantity in ingredients:
            ingredient = IngredientFactory.create_ingredient(ingredient_name, quantity)
            recipe.add_ingredient(ingredient)
        recipe.set_instructions(instructions)
        return recipe


def main() -> None:
    """
    Main function to create and display recipes in the cookbook.
    """
    cookbook = Cookbook()

    pancake_recipe = RecipeFactory.create_recipe(
        "Pancakes",
        [("Flour", "2 cups"), ("Milk", "1.5 cups"), ("Eggs", "2")],
        "1. Mix all ingredients.\n2. Pour batter onto hot griddle.\n3. Cook until golden brown."
    )
    cookbook.add_recipe(pancake_recipe)

    smoothie_recipe = RecipeFactory.create_recipe(
        "Smoothie",
        [("Banana", "1"), ("Milk", "1 cup"), ("Honey", "1 tbsp")],
        "1. Blend all ingredients until smooth."
    )
    cookbook.add_recipe(smoothie_recipe)

    print("All recipes in the cookbook:")
    cookbook.display_all_recipes()

    ingredient_to_search = "Milk"
    print(f"\nRecipes with ingredient '{ingredient_to_search}':")
    recipes_with_milk = cookbook.find_recipes_by_ingredient(ingredient_to_search)
    for recipe in recipes_with_milk:
        recipe.display()


if __name__ == "__main__":
    main()
