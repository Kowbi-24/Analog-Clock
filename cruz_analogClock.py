import turtle 
import time

def setUpWindow():
    window = turtle.Screen()
    window.bgcolor("black")
    window.setup(width=600, height=600)
    window.title("Analog Clock")
    window.tracer(0)

    return window

def createDrawingPen():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(3)

    return pen

def drawClock(pen, hour, minute, second):
    faceColor = "white"
    hourHandColor = "white"
    minuteHandColor = "white"
    secondHandColor = "red"

    hourLineColor = "white"
    secondLineColor = "white"
    
    # Drawing the clock face
    pen.up()
    pen.goto(0 , 210)
    pen.setheading(180)
    pen.color(faceColor)
    pen.pendown()
    pen.circle(210)

    # Draw lines for hours
    pen.pensize(6)
    pen.color(hourLineColor)
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)
    for i in range(12):
        pen.fd(165)
        pen.fd(20)
        pen.pendown()
        pen.fd(23)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    # Draw lines for seconds
    pen.pensize(3)
    pen.color(secondLineColor)
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)
    for i in range(60):
        if (i%5 == 0):
            pen.rt(6)
            continue
        pen.fd(190)
        pen.pendown()
        pen.fd(10)
        pen.penup()
        pen.goto(0,0)
        pen.rt(6)

    # Draw hour hand
    pen.pensize(6)
    pen.penup()
    pen.goto(0,0)
    pen.color(hourHandColor)
    pen.setheading(90)
    angle = (hour / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)


    # Draw minute hand
    pen.pensize(3)
    pen.penup()
    pen.goto(0,0)
    pen.color(minuteHandColor)
    pen.setheading(90)
    angle = (minute / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(170)

    # Draw second hand
    pen.penup()
    pen.goto(0,0)
    pen.color(secondHandColor)
    pen.setheading(90)
    angle = (second / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)



def main():
    # Initialize important variables
    window = setUpWindow()
    pen = createDrawingPen()

    while True:
        # Get the time
        hour = int(time.strftime("%I"))
        minute = int(time.strftime("%M"))
        second = int(time.strftime("%S"))

        drawClock(pen,hour, minute, second)

        window.update() # Stores the drawing in memory, then pulls it to the screen
        pen.clear() # Clear the screen every frame
        time.sleep(0.1) # Delay the loop every 1/10th of a second

    


try:
    main()
except:
    pass