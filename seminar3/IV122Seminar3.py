import Commons
import math
import IV122Graphics


def drawNpolygon(name, n, length):
    
    turtle = IV122Graphics.Turtle(name,  400, 400, 200, 200)
    for i in range(n):
        turtle.forward(length)
        turtle.left(360/n)
    turtle.close()

def drawStar(name, n, length): #works only for odd n >=3
    turtle = IV122Graphics.Turtle(name,  400, 400, 50, 200)

    if (n%2 ==0 and (n/2)%2 == 1):
        upperLim = n*2
        x = 1
        div = n
    elif (n%4 == 0):
        upperLim = 2*n
        x = 2
        div = n
    else:
        upperLim = n
        x=2
        div = n
    for i in range(upperLim):
        turtle.forward(length)
        turtle.left(180 - (360/n)/x)
    turtle.close()
        
def pentagramRelative():
    turtle = IV122Graphics.Turtle("sem3/pentaInPenta.svg",  400, 400, 50, 200)
    n = 5
    length = 100
    for i in range(n):
        turtle.forward(length)
        turtle.left(360/n)
    turtle.left(360/n + 180 + (180 - 360/(2*n)))
    a = length * math.sin(Commons.degToRad(360/n))
    b = length * math.cos(Commons.degToRad(360/n))
    length = math.sqrt((100+b)**2 + a**2)
    for i in range(n):
        turtle.forward(length)
        turtle.left(180 - (360/n)/2)
    turtle.close()

def pentagramAbsolute():
    length = 100
    points = [(50,200)]
    n = 5
    orientation = 90
    svg = IV122Graphics.SVG("sem3/absolute.svg", 400, 400)
    for i in range(n-1): #from turtle
        newX = length * math.sin(Commons.degToRad(orientation))  + points[-1][0]
        newY = length * math.cos(Commons.degToRad(orientation))  + points[-1][1]
        orientation += 360/n
        points.append((newX, newY))

    for target in points:
        svg.circle(20, target[0], target[1])
    for i in range(0,len(points)):
        for target in points[i+1:]:
            svg.line(points[i][0], points[i][1], target[0], target[1])
    svg.close()


def squareInception(size = 200.0, percent = 20.0, nesting = 10.0):
    turtle = IV122Graphics.Turtle("sem3/squareInception.svg",  400, 400, 50, 300)
    curSize = size
    for level in range(nesting):
        for i in range(4):
            turtle.forward(curSize)
            turtle.left(90)
        turtle.forward(curSize*percent/100.0)
        a = (curSize*percent/100.0) 
        b = (curSize*(1-percent/100.0)) 
        angle = Commons.radToDeg(math.atan(a/b))
        turtle.left(angle)
        curSize = math.sqrt(a**2 +b**2)
    turtle.close()

      
def gridInCircle(radius = 200, delta = 10):
    svg = IV122Graphics.SVG("sem3/gridInCircle.svg",  radius*2, radius*2)
    x = radius
    y = radius
    for curY in range(-radius, radius, delta):
        distFromMiddle = math.sqrt( (radius*1.0)**2.0 - (curY*1.0)**2)
        svg.line( x - distFromMiddle, y+curY, x +distFromMiddle , y+curY)
        svg.line( x + curY, y-distFromMiddle, x + curY ,y+distFromMiddle)

    svg.close()

def triangleInception(size =200, d = 10):
    turtle = IV122Graphics.Turtle("sem3/triangleInception.svg",  400, 400, 50, 300)
    curSize = size
    for i in range( size / (d*2)):
        for i in range(3):
            turtle.forward(curSize)
            turtle.left(120)
        turtle.penUp()
        turtle.forward(d)
        turtle.left(90)
        turtle.forward(d *(2.0/3) *  (math.sqrt(3.0)/2.0))
        turtle.right(90)
        turtle.penDown()
        curSize = curSize - 2*d
    turtle.close()
    

def fractalBush(turtle, length, n):
    turtle.forward(length)
    if (n == 0):
        turtle.back(length)
        return
    turtle.left(45)
    fractalBush(turtle, length/2.0, n-1)
    turtle.right(90)
    fractalBush(turtle, length/2.0, n-1)
    turtle.left(45)
    turtle.back(length)

def fractalBushExecute():
    bushTurtle = IV122Graphics.Turtle("sem3/fractal/bush.svg",  400, 400, 200, 300)
    bushTurtle.left(90)
    fractalBush(bushTurtle, 128, 8)
    bushTurtle.close()

    
def kochSnowFlake(turtle,size,  deg):
    if (deg == 0):
        turtle.forward(size)
        return
    kochSnowFlake(turtle, size/3, deg-1)
    turtle.right(60)
    kochSnowFlake(turtle, size/3, deg-1)
    turtle.left(120)
    kochSnowFlake(turtle, size/3, deg-1)
    turtle.right(60)
    kochSnowFlake(turtle, size/3, deg-1)

def kochSnowflakeExecute():
    snowFlake = IV122Graphics.Turtle("sem3/fractal/koch.svg",  1000, 1000, 400, 500)
    for i in range(3):
        kochSnowFlake(snowFlake, 400,  5)
        snowFlake.left(120)
    snowFlake.close()
    
def sierpinskiTriangle(turtle,size,  deg):
    if (deg == 0):
        for i in range(3):
            turtle.penDown()
            turtle.forward(size)
            turtle.left(120)
            turtle.penDown()
        return
    sierpinskiTriangle(turtle, size/2, deg-1)
    turtle.forward(size/2)
    sierpinskiTriangle(turtle, size/2, deg-1)
    turtle.left(120)
    turtle.forward(size/2)
    turtle.right(120)
    sierpinskiTriangle(turtle, size/2, deg-1)
    turtle.right(120)
    turtle.forward(size/2)
    turtle.left(120)

def sierpinskiTriangleExecute():
    sierp = IV122Graphics.Turtle("sem3/fractal/sierp.svg",  1000, 1000, 400, 500)
    sierpinskiTriangle(sierp, 200,  5)
    sierp.close()

def pentagonIncpetion(turtle, size, n):
    if (n == 0):
        for i in range(5):
            turtle.penDown()
            turtle.forward(size)
            turtle.left(360/5)
            turtle.penUp()
        return
    pentagonIncpetion(turtle, size, n-1)
    turtle.forward(size)
    turtle.left(180)
    for i in range(5):
        pentagonIncpetion(turtle, size, n-1)
        turtle.left(252)
        turtle.forward(size)
        turtle.left(180)
    return

def pentagonIncpetionExecute():
    pentaDrawer = IV122Graphics.Turtle("sem3/fractal/pentagon.svg",  1000, 1000, 400, 500)
    pentagonIncpetion(pentaDrawer, 100,  2)
    pentaDrawer.close()
    
def turtleCreativity(turtle,size,  deg):
    if (deg == 0):
        return
    for i in range(3):
        turtleCreativity(turtle, size/3, deg-1)
        turtle.forward(size)
        turtle.right(60)
        turtle.forward(size)
        turtle.left(120)
        turtle.forward(size)
        turtle.right(60)
        turtle.forward(size)
        turtle.left(120)

def creativity2(turtle,size,  deg):
    if (deg == 0):
        turtle.forward(size)
        return
    for i in range(3):
        creativity2(turtle, size/3, deg-1)
        turtle.right(60)
        creativity2(turtle, size/3, deg-1)
        turtle.left(120)
        creativity2(turtle, size/3, deg-1)
        turtle.right(60)
        creativity2(turtle, size/3, deg-1)
        turtle.left(120)

def creativity2Execute():
    somethign = IV122Graphics.Turtle("sem3/fractal/creative2.svg",  400, 400, 200, 200)
    creativity2(somethign, 800,  4)
    somethign.close()
    
def turtleCreativityExecute():
    triangleFractal = IV122Graphics.Turtle("sem3/fractal/creativeTriangle.svg",  10000, 10000, 5000, 5000)
    turtleCreativity(triangleFractal, 800,  8)
    triangleFractal.close()
#fraktaly ker , vlocka, sierp, petiuhelnik, pak ty dalsi jsou spis pro zajimavostj
if __name__ == "__main__":
    for i in range(2,20):
        drawNpolygon("sem3/poly/polygon" + str(i) + ".svg", i, 100)
        drawStar("sem3/stars/star" + str(i) + ".svg", i, 100)
    turtle = IV122Graphics.Turtle("sem3/test.svg",  400, 400, 50, 300)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.back(25)
    turtle.left(90)
    turtle.forward(10)
    turtle.close()

    pentagramRelative()
    pentagramAbsolute()
    squareInception(200, 20, 20)
    gridInCircle()
    triangleInception()

    fractalBushExecute()
    kochSnowflakeExecute()
    sierpinskiTriangleExecute()
    #turtleCreativityExecute()
    #creativity2Execute()

    pentagonIncpetionExecute()
