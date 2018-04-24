# list of savoury recipes available
import kitchencontents
import recipes
import sys


available_recipes = []


def savoury_options():

    for meal, item in recipes.savoury_recipes.items():
        if item.issubset(kitchencontents.food_in_my_kitchen):
            available_recipes.append(meal)
            continue
    if not available_recipes:
        print("sorry no recipes available")
        sys.exit(0)
    else:
        print("Available recipes: {}".format(available_recipes))
        available_recipes_choice()


def available_recipes_choice():
    recipe_number = input("please choose meal number from 1 - {} \n".format(len(available_recipes)))
    recipe_number = int(recipe_number) - 1
    print("You have chosen {}".format(available_recipes[recipe_number]))
