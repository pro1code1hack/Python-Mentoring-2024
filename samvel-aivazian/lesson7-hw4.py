from typing import List


class Ingredient:
    def __init__(self, name: str, quantity: str) -> None:
        self.name: str = name
        self.quantity: str = quantity


class Recipe:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.ingredients: List[Ingredient] = []
        self.instructions: str = ""

    def add_ingredient(self, ingredient: Ingredient) -> None:
        self.ingredients.append(ingredient)

    def set_instructions(self, instructions: str) -> None:
        self.instructions = instructions

    def display(self) -> None:
        print(f"Recipe: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"{ingredient.name}: {ingredient.quantity}")
        print("Instructions:")
        print(self.instructions)


class Cookbook:
    def __init__(self) -> None:
        self.recipes: List[Recipe] = []

    def add_recipe(self, recipe: Recipe) -> None:
        self.recipes.append(recipe)

    def find_recipes_by_ingredient(self, ingredient_name: str) -> List[Recipe]:
        found_recipes = []
        for recipe in self.recipes:
            for ingredient in recipe.ingredients:
                if ingredient.name == ingredient_name:
                    found_recipes.append(recipe)
                    break
        return found_recipes

    def display_all_recipes(self) -> None:
        if not self.recipes:
            print("No recipes in the cookbook.")
        for recipe in self.recipes:
            recipe.display()


def main() -> None:
    cookbook: Cookbook = Cookbook()

    pancake_recipe: Recipe = Recipe("Pancakes")
    pancake_recipe.add_ingredient(Ingredient("Flour", "2 cups"))
    pancake_recipe.add_ingredient(Ingredient("Milk", "1.5 cups"))
    pancake_recipe.add_ingredient(Ingredient("Eggs", "2"))
    pancake_recipe.set_instructions(
        "1. Mix all ingredients.\n2. Pour batter onto hot griddle.\n3. Cook until golden brown."
    )
    cookbook.add_recipe(pancake_recipe)

    smoothie_recipe: Recipe = Recipe("Smoothie")
    smoothie_recipe.add_ingredient(Ingredient("Banana", "1"))
    smoothie_recipe.add_ingredient(Ingredient("Milk", "1 cup"))
    smoothie_recipe.add_ingredient(Ingredient("Honey", "1 tbsp"))
    smoothie_recipe.set_instructions("1. Blend all ingredients until smooth.")
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
