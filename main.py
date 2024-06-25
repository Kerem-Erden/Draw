import turtle

turtleScreen = turtle.Screen()
turtleScreen.bgcolor("White")
turtleScreen.title("Drawing Game Turtle")

turtleInstance = turtle.Turtle()

def turtleForward():
    turtleInstance.forward(50)

def turtleTurnRight():
    turtleInstance.right(50)

def turtleTurnLeft():
    turtleInstance.left(20)

turtleColors = ["green", "red", "purple", "yellow", "black", "brown", "blue"]
n = -1
def changeTurtleColor():
    global n
    n = (n + 1) % len(turtleColors)
    turtleInstance.color(turtleColors[n])

w = 1
def turtleThicker():
    global w
    w += 1
    turtleInstance.width(width= w)

def turtleThin():
    global w
    if w > 1:
        w -= 1
        turtleInstance.width(width= w)

def clearScreen():
    turtleInstance.clear()

def returnMainBase():
    turtleInstance.penup()
    turtleInstance.home()
    turtleInstance.pendown()

turtleScreen.listen()
turtleScreen.onkey(fun= turtleForward, key= "space")
turtleScreen.onkey(fun= turtleTurnRight, key= "Right")
turtleScreen.onkey(fun= turtleTurnLeft, key= "Left")
turtleScreen.onkey(fun= changeTurtleColor, key= "c")
turtleScreen.onkey(fun= turtleThicker, key= "z")
turtleScreen.onkey(fun= turtleThin, key= "x")
turtleScreen.onkey(fun= clearScreen, key= "a")
turtleScreen.onkey(fun= returnMainBase,key= "r")




turtle.mainloop()