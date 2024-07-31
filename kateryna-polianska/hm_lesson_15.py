"""
Task 4: Recipe System

Design a system to create, store, and display recipes, including ingredients, quantities, and cooking instructions.

Classes:
1. Ingredient
2. Recipe
3. Cookbook

Functionalities:
1. Add new recipes
2. Find recipes by ingredient
3. Display all recipes
4. Search for recipes based on available ingredients
"""

class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.quantity} of {self.name}"

class Recipe:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def __str__(self):
        ingredients_list = '\n'.join(str(ingredient) for ingredient in self.ingredients)
        return f"Recipe: {self.name}\nIngredients:\n{ingredients_list}\nInstructions: {self.instructions}"

class Cookbook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def find_recipes_by_ingredient(self, ingredient_name):
        return [recipe for recipe in self.recipes if any(ingredient.name == ingredient_name for ingredient in recipe.ingredients)]

    def display_all_recipes(self):
        return '\n\n'.join(str(recipe) for recipe in self.recipes)

    def search_recipes_by_ingredients(self, available_ingredients):
        available_ingredients_set = set(available_ingredients)
        return [recipe for recipe in self.recipes if available_ingredients_set.issuperset({ingredient.name for ingredient in recipe.ingredients})]

def main():
    cookbook = Cookbook()

    while True:
        print("\nMenu:")
        print("1. Add a new recipe")
        print("2. Find recipes by ingredient")
        print("3. Display all recipes")
        print("4. Search recipes by available ingredients")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            name = input("Enter the recipe name: ").strip()
            instructions = input("Enter the cooking instructions: ").strip()
            recipe = Recipe(name, instructions)

            while True:
                ingredient_name = input("Enter ingredient name (or type 'done' to finish): ").strip()
                if ingredient_name.lower() == 'done':
                    break
                quantity = input(f"Enter quantity for {ingredient_name}: ").strip()
                ingredient = Ingredient(ingredient_name, quantity)
                recipe.add_ingredient(ingredient)

            cookbook.add_recipe(recipe)
            print(f"Recipe '{name}' added successfully!")

        elif choice == '2':
            ingredient_name = input("Enter the ingredient name to search for: ").strip()
            recipes = cookbook.find_recipes_by_ingredient(ingredient_name)
            if recipes:
                print(f"Recipes containing '{ingredient_name}':\n")
                for recipe in recipes:
                    print(recipe)
            else:
                print(f"No recipes found with the ingredient '{ingredient_name}'.")

        elif choice == '3':
            all_recipes = cookbook.display_all_recipes()
            print(f"All Recipes:\n{all_recipes}")

        elif choice == '4':
            available_ingredients = input("Enter available ingredients (separated by comma): ").strip().split(',')
            available_ingredients = [ingredient.strip() for ingredient in available_ingredients]
            recipes = cookbook.search_recipes_by_ingredients(available_ingredients)
            if recipes:
                print("Recipes you can make with the available ingredients:\n")
                for recipe in recipes:
                    print(recipe)
            else:
                print("No recipes found with the available ingredients.")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
