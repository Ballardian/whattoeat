import kitchencontents
import recipes
import sys





# def savoury_options():
#     for meal, item in recipes.savoury_recipes.items():
#         if item.issubset(kitchencontents.food_in_my_kitchen):
#             available_recipes.append(meal)
#             continue
#     if not available_recipes:
#         print("sorry no recipes available")
#         sys.exit(0)
#     else:
#         print("Available recipes: \n")
#         for number, meal in enumerate(available_recipes):
#             print("{}. {} \n".format((number+1), meal))
#         available_recipes_choice()
#
#
# def available_recipes_choice():
#     recipe_number = input("You have {} meal option(s)."
#                           " Please pick a number. \n".format(len(available_recipes)))
#     while recipe_number.isalpha() or int(recipe_number) > len(available_recipes) or int(recipe_number) <= 0:
#         print("please enter a number corresponding to a recipe")
#         recipe_number = input("You have {} meal option(s)."
#                               " Please pick a number. \n".format(len(available_recipes)))
#
#     recipe_number = int(recipe_number) - 1
#     print("You have chosen {}.".format(available_recipes[recipe_number]))

