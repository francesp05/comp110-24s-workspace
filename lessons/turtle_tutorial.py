"""Turtle tutorial."""

from turtle import Turtle, colormode, done      # import turtle functions and class
leo: Turtle = Turtle()      # create variable (leo) bound to a turtle object
colormode(255)      #To enable RGB mode

# to make the turtle do anything, use syntax: turtle_object_variable.method_name()
'''leo.forward(50)
leo.left(30)
leo.right(40)

done()'''      #makes sure window doesnt close until this function. The done() function must come after all the turtle functions you want to see in a window


## EX01: DRAW A SQUARE
'''leo.forward(50)
leo.left(90)
leo.forward(50)
leo.left(90)
leo.forward(50)
leo.left(90)
leo.forward(50)

done()

#to simplify this process, repeat something a certain number of times: while (<counter_variable> < <number_of_times>)
i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1'''

##EX02: CONVERT LOOP TO TRIANGLE
'''i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1'''

# To move the turtle to a new x, y position: <turtlevariable>.goto(<x_coordinate>,<y_coordinate>)
'''leo.goto(45, 60)''' #results in an unwanted line

'''leo.penup()     # To prevent the turtle from drawing: <turtlevariable>.penup() or <turtlevariable>.up()
leo.goto(0, 0)        #moves turtle to desired start point
leo.pendown()       #To allow the turtle to draw: <turtlevariable>.pendown() or <turtlevariable>.down()
 
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

# To change the color with a string value: <turtlevariable>.color(“<color>”)
leo.color(99, 204, 250) #before turtle functions

leo.begin_fill()
# code for shape to be filled 
leo.end_fill()

# To set only pen color: <turtlevariable>.pencolor(<color>)
leo.pencolor("pink")
# To set only fill color: <turtlevariable>.fillcolor(<color>)
leo.fillcolor(32, 67, 93)
# To set fill and pen color: <turtlevariable>.color(<pencolor>, <fillcolor>)
leo.color("green", "yellow")
'''
'''##EX03: fill triangle

leo.color(255, 0, 0)
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

done()'''

'''# To change the speed: <turtlevariable>.speed(<speed>)
leo.speed(50)
# To end fill: <turtlevariable>.hideturtle() or <turtlevariable>.ht()
leo.hideturtle()'''

##MINI-PROJECT
side_length = 300
leo.hideturtle()
leo.speed(50)
leo.color(255, 0, 0)
leo.begin_fill()

i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
bob.hideturtle()
bob.speed(200)
bob.color(0, 0, 0)

i: int = 0
while (i < 250):
    bob.forward(side_length * 0.95)
    bob.left(121)
    i = i + 1

done()