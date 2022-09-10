import turtle


colors = ["red","white","purple","blue","green","yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
turtle.title("Graphics")
turtle.speed(100)
for x in range(100):
    my_pen.pencolor(colors[x % 6])
    my_pen.width(x/200 + 2)
    my_pen.forward(x)
    my_pen.left(59)



'''
    
my_wn = turtle.screensize()
turtle.speed(2)
for i in range(30):

    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
turtle.exitonclick()
'''