"""Cute turtle scene using recursion yay."""

__author__ = "730672003"

import turtle
from turtle import Turtle, colormode, done
colormode(255)


def draw_rect(grass: Turtle, x: float, y: float, width: int, height: int, color: str) -> None:
    """Above and Beyond: Function used to simplify the complex draw_grass and draw_tree function."""
    grass.penup()
    grass.goto(x, y)  
    grass.pendown()
    grass.color(color)
    grass.begin_fill()
    i: int = 0
    while (i < 2):
        grass.forward(width)
        grass.left(90)
        grass.forward(height)
        grass.left(90)
        i = i + 1
    grass.end_fill()


def draw_grass(grass: Turtle, x: float, y: float) -> None:
    """Fill bottom fourth of the screen with green for the grass of this scene by calling draw_rect."""
    draw_rect(grass, -400.0, -300.0, 800, 150, "green")


def draw_tree(tree: Turtle, x: float, y: float) -> None:
    """Draw trees for something drawn at least twice."""
    tree.penup()
    tree.goto(x, y)  
    tree.pendown()

    # draw the trunk
    # draw_rect(tree, x, y, 20, 100, "brown")
    tree.color(108, 56, 0)
    tree.begin_fill()
    tree.setheading(90)  
    tree.forward(100)  
    tree.right(90)  
    tree.forward(20)  
    tree.right(90)  

    """Above and Beyond: using the ycor() function to save the current postion to draw the leaves for other trees"""
    trunk_top = tree.ycor()

    tree.forward(100)  
    tree.end_fill()

    # draw the leaves
    tree.penup()
    tree.goto(x, trunk_top)  
    tree.setheading(60)  
    tree.color(0, 86, 17)
    tree.begin_fill()
    tree.pendown()
    i: int = 0
    while (i < 3):
        tree.forward(80)
        tree.left(120)
        i = i + 1
    tree.end_fill()


def draw_sun(sun: Turtle, x: float, y: float) -> None:
    """Draw the sun as a square filled with yellow."""
    sun.penup()
    sun.goto(x, y)  
    sun.pendown()
    sun.color("yellow")
    sun.begin_fill()
    i = 0
    while (i < 4):
        sun.forward(100)
        sun.left(90)
        i = i + 1
    sun.end_fill()


def draw_moon(moon: Turtle, x: float, y: float) -> None:
    """Draw the moon as a square filled with dark gray."""
    moon.penup()
    moon.goto(x, y)  
    moon.pendown()
    moon.color("dark gray")
    moon.begin_fill()
    i = 0
    while (i < 4):
        moon.forward(100)
        moon.left(90)
        i = i + 1
    moon.end_fill()


def main() -> None:
    """Call all the functions I made to create the scene."""
    # set up screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)  
    screen.bgcolor("sky blue")  

    # create a turtle for drawing
    pen = turtle.Turtle()
    pen.speed(0)  

    # draw grass
    draw_grass(pen, -400.0, -300.0)

    # draw three trees
    draw_tree(pen, -300.0, -150.0)  
    draw_tree(pen, 0.0, -150.0)     
    draw_tree(pen, 300.0, -150.0)   

    # draw the sun
    draw_sun(pen, -250.0, 150.0)

    # draw the moon == ECLIPSE WOAAAHWOAHOWAHOW
    draw_moon(pen, -200.0, 150.0)

    # hide the turtle and display the result
    pen.hideturtle()
   
    done()


if __name__ == "__main__":
    main()
