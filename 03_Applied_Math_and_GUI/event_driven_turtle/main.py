import turtle
import random

Score = 0

gameBoard = turtle.Screen()
gameBoard.bgcolor("Light blue")
gameBoard.title("Welcome to Catch The Turtle Game!")

timeRemaining = int(gameBoard.numinput("Welcome The Game", "Chose The Game Time!", minval= 10, maxval=60 ))

gameInstance = turtle.Turtle()
gameInstance.shape("turtle")
gameInstance.color("green")
gameInstance.penup()
gameInstance.speed(0)

gamePointCounter = turtle.Turtle()
gamePointCounter.hideturtle()
gamePointCounter.penup()
gamePointCounter.goto(0,250)

timeWriter = turtle.Turtle()
timeWriter.hideturtle()
timeWriter.penup()
timeWriter.goto(0,200)

def countDown():
    global timeRemaining
    timeRemaining = timeRemaining - 1
    updateTimeDisplay()

    if timeRemaining > 0:
        gameBoard.ontimer(countDown, 1000)

    else:
        gameInstance.hideturtle()
        timeWriter.goto(0,0)
        timeWriter.write(f"Game Over! Your Score: {Score}", align="Center", font=("Arial", 50, "normal"))
        gameInstance.onclick(None)

def moveTurtle():
    gameInstance.hideturtle()

    kx = random.randint(-200, 200)
    ky = random.randint(-200, 200)
    gameInstance.goto(kx, ky)

    gameInstance.showturtle()
    gameBoard.ontimer(moveTurtle, 1000)


def updateTimeDisplay():
    timeWriter.clear()
    timeWriter.write(f" time: {timeRemaining}", align="center", font=("Arial", 20, "normal"))
    print(timeRemaining)

def updateScore():
    gamePointCounter.clear()
    gamePointCounter.write(f" Score: {Score}", align= "center", font=("Arial", 20 , "normal"))


def turtleClick(x,y):
    global Score
    Score = Score + 1
    updateScore()
    print(Score)



gameInstance.onclick(turtleClick)

updateScore()
updateTimeDisplay()
countDown()
moveTurtle()

turtle.mainloop()