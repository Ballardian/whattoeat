# ''' Recipes '''
# # TODO add cooking instructions

import json
import sweet
import savoury
import kitchencontents
#
# fajitas = {"chicken", "wraps", "pepper", "onions", "spinach"}
# stew = {"chicken", "pepper", "onions", "spinach", "tomatoes"}
#
# savoury_recipes = {"Fajitas": {"chicken", "wraps", "pepper", "onions", "spinach"},
#                    "Stew": {"chicken", "pepper", "onions", "spinach", "tomatoes"},
#                    "Poached eggs": {"eggs", "bread"},
#                    "Full English": {"sausages", "beans", "eggs", "bread"}}


class Recipe:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.meal_name

    def __repr__(self):
        return str(self)


def get_recipes(filename, raw=False):
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data['recipe_test']
        return [Recipe(**meal) for meal in data['recipes_test']]


RECIPES = get_recipes('contents.json')
# print(RECIPES[2])


def is_in_kitchen(meal):
    return set(meal.ingredients).issubset(kitchencontents.food_in_my_kitchen)


def meal_options():
    list_of_meals = list(filter(is_in_kitchen, RECIPES))
    for number, meal in enumerate(list_of_meals):
        print("{}. {}".format((number+1), meal))
    return list_of_meals


def meal_choice():
    choices = meal_options()
    recipe_number = input("You have {} meal option(s)."
                          " Please pick a number. \n".format(len(choices)))
    recipe_number = int(recipe_number) - 1
    print("You have chosen {}.".format(choices[recipe_number]))
    chosen_meal = RECIPES[recipe_number]
    return chosen_meal


def display_meal_details():
    meal_ingredients = meal_choice()
    print("The prep time of your meal is {} minutes.".format(meal_ingredients.prep_time))
    print("The cooking time of your meal is {} minutes.".format(meal_ingredients.cook_time))
    print("The ingredients of your meal are {}".format(meal_ingredients.ingredients))


# meal_options()
display_meal_details()

#print(RECIPES[0].ingredients)
