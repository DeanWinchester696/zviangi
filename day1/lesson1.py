from turtle import *


#we want to paint a house

#step1 draw a square

width(7)
color("purple")
begin_fill()
speed(30)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("blue")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()



penup()
goto(200,200)
pendown()

color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#window1
penup()
color("red")
begin_fill()
goto(20, 135)
pendown()
left(120)
forward(35)
left(90)
forward(40)
left(90)
forward(35)
left(90)
forward(40)
end_fill()

#window2
penup()
color("red")
begin_fill()
goto(140, 135)
pendown()
left(90)
forward(35)
left(90)
forward(40)
left(90)
forward(35)
left(90)
forward(40)
end_fill()




exitonclick()