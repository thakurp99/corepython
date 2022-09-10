import turtle
from turtle import *

color("Red","yellow")
bgcolor("blue")
begin_fill()
while True:
    speed(100)
    forward(350)
    left(170)
    if abs(pos()) < 5:
        break
end_fill()
done()