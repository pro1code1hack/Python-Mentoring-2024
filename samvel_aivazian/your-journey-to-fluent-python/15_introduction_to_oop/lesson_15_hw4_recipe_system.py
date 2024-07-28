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


class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    @execution_time_decorator
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    @execution_time_decorator
    def display_recipe(self):
        logging.info(f"Recipe: {self.name}")
        for ingredient in self.ingredients:
            logging.info(f"{ingredient.quantity} of {ingredient.name}")


class Cookbook:
    def __init__(self):
        self.recipes = []

    @execution_time_decorator
    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        logging.info(f"Recipe added: {recipe.name}")

    @execution_time_decorator
    def find_recipes_by_ingredient(self, ingredient_name):
        found_recipes = []
        for recipe in self.recipes:
            for ingredient in recipe.ingredients:
                if ingredient.name == ingredient_name:
                    found_recipes.append(recipe)
                    break
        return found_recipes

    @execution_time_decorator
    def display_recipes(self):
        for recipe in self.recipes:
            recipe.display_recipe()


if __name__ == "__main__":
    cookbook = Cookbook()

    recipe1 = Recipe("Pancakes")
    recipe1.add_ingredient(Ingredient("Flour", "2 cups"))
    recipe1.add_ingredient(Ingredient("Milk", "1 cup"))
    recipe1.add_ingredient(Ingredient("Eggs", "2"))

    recipe2 = Recipe("Omelette")
    recipe2.add_ingredient(Ingredient("Eggs", "3"))
    recipe2.add_ingredient(Ingredient("Cheese", "1/2 cup"))

    cookbook.add_recipe(recipe1)
    cookbook.add_recipe(recipe2)

    cookbook.display_recipes()

    logging.info("Recipes with Eggs:")
    egg_recipes = cookbook.find_recipes_by_ingredient("Eggs")
    for recipe in egg_recipes:
        recipe.display_recipe()
