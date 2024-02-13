from turtle import *

speed('fastest')
pencolor('blue')
pensize(4)
for i in range(10):
    fd(120)
    lt(360/10)
    write(f'n={i}')
hideturtle()
mainloop()