from turtle import Turtle, Screen
import random


is_race_on = False

screen = Screen()
screen.setup(width=1000, height=600)
liner = Turtle()
liner.penup()
liner.goto(x=-485,y=0)
liner.pendown()
liner.goto(y=300, x=-485)
liner.goto(y=-300, x=-485)
liner.penup()
liner.goto(x=485,y=0)
liner.pendown()
liner.goto(y=300, x=485)
liner.goto(y=-300, x=485)


user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []


for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-485, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on= True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 485:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won!. The {winning_color} turtle is the winner!")
            else:
                print(f"you lost!. The {winning_color} turtle is the winner!")

        turtle.forward(random.randint(0,10))


screen.exitonclick()
