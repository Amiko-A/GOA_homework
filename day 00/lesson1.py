print("day 1 homework")
from turtle import*
#making spueare
width(5)
begin_fill()
color("black")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()
#end of spuere
#making door for house
begin_fill()
left(90)
forward(70)
color("brown")
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()
color("black")
#finished making door
#making windows
left(90)
forward(80)
left(90)
forward(100)
begin_fill()
color("cyan")
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
#finished  making first window
#started making  roof
penup()
goto(200,200)
pendown()
color("red")
begin_fill()
left(120)
forward(200)
left(120)
forward(200)
end_fill()
#finished making roof 
#started making second window
color("black")
begin_fill()
left(30)
forward(100)
color("cyan")
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
speed(0.50)
exitonclick()