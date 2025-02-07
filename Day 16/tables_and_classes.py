# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
#
# # attributing the class Turtle() to the object timmy
# timmy = Turtle()
# print(timmy)
#
# # Choosing turtle format -> object.method
# timmy.shape("turtle")
# timmy.color("blue")
#
# # attributing the class Screen() to the object my_screen
# my_screen = Screen()
# print(my_screen.canvheight) # Printing an attribute -> object.attribute
#
# # Drawing a square
# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)
#     timmy.screen.delay(30)
#
# my_screen.exitonclick()

from prettytable import PrettyTable # Importing class PrettyTable

table = PrettyTable() # Creating an object

table.add_column("Pokemon name", ['Pikachu', "Squirtle", 'Charizard'])
table.add_column("Type", ['Eletric', "Water", 'Fire'])

table.align = "l"

print(table)

