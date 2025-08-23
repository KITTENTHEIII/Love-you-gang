import turtle as t

t.bgcolor("black")
t.pensize(5)
t.speed(1)
t.color("red")
t.begin_fill()
t.fillcolor("red")

t.left(150)
t.forward(180)
t.circle(-90, 180)
t.setheading(60)
t.circle(-90, 180)
t.forward(180)

t.end_fill()
t.hideturtle()

# Text message
msg = "   I LOVE YOU"
font = ("Arial", 25, "italic", "bold")
t.penup()
t.goto(-70, -50)
t.pendown()
t.write(msg, move=True, align="left", font=font)

t.done()
