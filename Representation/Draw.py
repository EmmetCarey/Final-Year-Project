from Tkinter import *
def Draw(pixels,n,size,length,width_new):

    t = 0
    import time
    count = 0
    total_time = length*0.000658853368294
    time.sleep(0.1)
    import turtle
    wn = turtle.Screen()
    myPen = turtle.Turtle()
    myPen.up()
    myPen.tracer(0)
    myPen.speed(0)
    myPen.goto(0, 0)
    boxSize = size
    myPen.penup()

    wn.screensize()
    height = 900
    wn.screensize(width_new+1000, height)
    wn.setup(width=1.0, height=1.0)
    print width_new


    def progressBar(value, endvalue, bar_length=20):

        percent = float(value) / endvalue
        arrow = '-' * int(round(percent * bar_length) - 1) + '>'
        spaces = ' ' * (bar_length - len(arrow))

        sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()

    def box(intDim):
        myPen.down()
        myPen.begin_fill()
        # 0 deg.
        myPen.forward(intDim)
        myPen.left(90)
        # 90 deg.
        myPen.forward(intDim)
        myPen.left(90)
        # 180 deg.
        myPen.forward(intDim)
        myPen.left(90)
        # 270 deg.
        myPen.forward(intDim)
        myPen.end_fill()
        myPen.setheading(0)



    for i in range(0, len(pixels)):
        for j in range(0, len(pixels[i])):
            if pixels[i][j] == 1:
                myPen.color("#ff0000")
            if pixels[i][j] == 2:
                myPen.color("#00ff00")
            if pixels[i][j] == 3:
                myPen.color("#0000ff")
            if pixels[i][j] == 4:
                myPen.color("#000000")
            count += 1
            start_time = time.clock()
            box(boxSize)
            myPen.penup()
            myPen.forward(boxSize)
            myPen.pendown()

            t += (time.clock() - start_time)


            progressBar(count,length,20)

        myPen.setheading(270)
        myPen.penup()
        myPen.forward(boxSize)
        myPen.setheading(180)
        myPen.forward(boxSize * len(pixels[i]))
        myPen.setheading(0)
        myPen.pendown()

    myPen.getscreen().update()
    if n == 0:
        ts = turtle.getscreen()
        #ts.getcanvas().postscript(file="duck.eps")
        ts.getcanvas().postscript(file="Conway_Stack.eps", colormode='color', pagewidth=900, pageheight=900, width=width_new * 2,
                                   height=900)
        wn.exitonclick()


