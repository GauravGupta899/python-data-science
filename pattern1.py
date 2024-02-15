from turtle import* 
speed(0)
def square():
    for i in range (4):
        forward(100)
        right(90)

def hexagon():
    for i in range (6):
        forward(100)
        right(60)

# def triangle():
#     for i in range (3):
#         forward(100)
#         right(120)

# triangle()
# for i in range(6):
#     fd(100)
#     hexagon()
#     square()
#     rt(60)

def octagon():
    for i in range(8):
        forward(100)
        right(360/8)
octagon()       

hideturtle()
mainloop()    


