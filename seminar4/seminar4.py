import sys, os, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parent = "/".join(cmd_folder.split("/")[0:-1])
parent += "/commonScripts"
sys.path.insert(0,parent)

import Commons
import IV122Graphics
import math

def circle(name, x,y, r, full = 0):
    size = 500
    bitmap = IV122Graphics.BitMap("output/shapes/" + name + ".jpg", size, size)
    thickness = 300.0
    
    for i_x in range(size):
        for i_y in range(size):
            if (full == 0):
                if  abs((float(i_x) - x)**2.0 + (i_y-y)**2  - r**2) <= thickness:
                    bitmap.putPixel(i_x, i_y, (100, 100, 100))
            else:
                if  abs((float(i_x) - x)**2.0 + (i_y-y)**2) <= thickness + r*r:
                    bitmap.putPixel(i_x, i_y, (100, 100, 100))
    bitmap.close()
    
def spiral(name, x,y, r, full = 0):
    size = 500
    bitmap = IV122Graphics.BitMap("output/shapes/" + name + ".jpg", size, size)
    
    #todo zmenit 20 na parametrizovatleny rozestup
    for t in range(360*5):
        i_x = (t/20) * math.sin(Commons.degToRad((t))) + x
        i_y = (t/20) * math.cos(Commons.degToRad((t))) + y
        bitmap.putPixel(i_x, i_y, (100, 100, 100))


    bitmap.close()

def colorEquilateralTriangle(name, size = 500):
    bitmap = IV122Graphics.BitMap("output/shapes/" + name + ".jpg", size, size)

    bot = 10
    right = size - 10
    left = 10

    for i_x in range(size):
        for i_y in range(size):
            halfplane1 = i_y >= 0
            #halfplane2 = i_y <= -math.sqrt(3.0)/2 * i_x + math.sqrt(3.0)*size/2
            halfplane2 = i_y >= math.sqrt(3.0) * i_x 
            halfplane3 = i_y >= -math.sqrt(3.0) * i_x  + size
            #halfplane3 = i_y <= math.sqrt(3.0)/2 * i_x + -math.sqrt(3.0)*size/2

            if (halfplane1 and halfplane2 and halfplane3):
                bitmap.putPixel(i_x, i_y, ((i_x/2)%255,(i_y/3)%255 , 100))
    bitmap.close()

def ellipses(name, size = 500):
    bitmap = IV122Graphics.BitMap("output/shapes/" + name + ".jpg", size, size)

    bot = 10
    right = size - 10
    left = 10

    for i_x in range(-size/2, size/2):
        for i_y in range(-size/2, size/2):
            a = 100
            b = 200

            term1 = ((i_x*Commons.cos(30) + i_y*Commons.sin(30))**2)/(a*a)
            term2 = ((i_x*Commons.sin(30) - i_y*Commons.cos(30))**2)/(b*b)

            distance = (i_x*i_x + i_y*i_y)**0.5

            if (term1 + term2 <= 1):
                bitmap.putPixel(size/2+i_x,size/2+ i_y, (255-distance, 255-distance, 255-distance))
    bitmap.close()


def countIntersect(p, lineSegments):
    result = 0

    for lineSeg in lineSegments:
        isInterseted = Commons.computeLineIntersection(p, (1,p[1]), lineSeg[0], lineSeg[1])
        if (isInterseted == -2): #rovnobezna usecka probably dont really care 
            return 0

        if(isInterseted != -1):
            result = result + 1



    return result

def drawFilledPolygon(points,name,  size):
    bitmap = IV122Graphics.BitMap("output/" + name + ".jpg", size, size)
    resultLineSegments = []
    for i in range(len(points)):
        resultLineSegments.append((points[i-1], points[i]))
    print resultLineSegments
    for i_x in range(size):
        for i_y in range(size):
            intersetCount = countIntersect((i_x, i_y), resultLineSegments)
            if (intersetCount % 2 == 1):
                bitmap.putPixel(i_x, i_y, (100,100, 100))

    bitmap.close()


def generateWeirdChessboard(name, size):
    bitmap = IV122Graphics.BitMap("output/effects/" + name + ".jpg", size, size)
    squareSize = 20
    black = (0,0,0) #initially black, but swaps during execution
    white = (0xFF, 0xFF, 0xFF)
    
    radiusSize = 50
    for i_x in range(-size/2, size/2):
        for i_y in range(-size/2, size/2):
            xParity = (i_x/20) % 2
            yParity = (i_y/20) % 2
            levelOfCircle = ((i_x**2 + i_y**2)**0.5)/radiusSize #v kolikatem krouzku od prostred jsem
            #print int(levelOfCircle)

            if(int(levelOfCircle)%2 == 0):
                color1, color2 = black, white
            else: 
                color1, color2 = white, black

            if(xParity == 1):
                if (yParity == 1):
                    print "a", color1, color2
                    bitmap.putPixel(size/2+ i_x,size/2+  i_y,color2)
                else:
                    print "b", color1, color2
                    bitmap.putPixel(size/2+ i_x,size/2+  i_y,color1)
            else:
                if (yParity == 1):
                    print "c", color1, color2
                    bitmap.putPixel(size/2+ i_x,size/2+  i_y,color1)
                else:
                    print "d", color1, color2
                    bitmap.putPixel(size/2+ i_x,size/2+  i_y,color2)

    print "neco"
    bitmap.close()

def generateWeirdCircles(name, size):
    bitmap = IV122Graphics.BitMap("output/effects/" + name + ".jpg", size, size)
    squareSize = 100
    black = (0,0,0) #initially black, but swaps during execution
    white = (0xFF, 0xFF, 0xFF)
    
    radiusSize = 50
    for i_x in range(-size/2, size/2):
        for i_y in range(-size/2, size/2):
            distanceFromMiddle = ((i_x**2 + i_y**2)**0.5)
            isInsideSquare = abs(i_x)<squareSize/2 and abs(i_y)<squareSize/2

            if(isInsideSquare):
                colElement =  127 + Commons.cos((360/radiusSize)*(distanceFromMiddle%radiusSize))*127
            else:
                colElement =  127 - Commons.cos((360/radiusSize)*(distanceFromMiddle%radiusSize))*127

        
            color = (colElement, colElement, colElement)

            bitmap.putPixel(size/2+ i_x,size/2+  i_y,color)

    print "neco"
    bitmap.close()

def generateWeirdStrips(name, size):
    bitmap = IV122Graphics.BitMap("output/effects/" + name + ".jpg", size, size)
    stripSize = 20
    
    radiusSize = 50
    for i_x in range(-size/2, size/2):
        for i_y in range(-size/2, size/2):
            distanceFromMiddle = ((i_x**2 + i_y**2)**0.5)
            isInsideSquare = abs(i_x)<squareSize/2 and abs(i_y)<squareSize/2

            if(isInsideSquare):
                colElement =  127 + Commons.cos((360/radiusSize)*(distanceFromMiddle%radiusSize))*127
            else:
                colElement =  127 - Commons.cos((360/radiusSize)*(distanceFromMiddle%radiusSize))*127

        
            color = (colElement, colElement, colElement)

            bitmap.putPixel(size/2+ i_x,size/2+  i_y,color)

    print "neco"
    bitmap.close()




if __name__ == "__main__":
   # circle("empty", 150,250,50, 0)
   # circle("full", 150,250,50, 1)
   # spiral("spiral", 250,250,50)
   # colorEquilateralTriangle("triangle")
    #drawFilledPolygon( [(10, 10), (180, 20), (160, 150), (100, 50), (20, 180)],"polygon",  400)

   #ellipses("ellipses1")
   # 
   #generateWeirdChessboard("chessboard", 500)
   #generateWeirdCircles("circlesWithSquareAsRequested", 500)
   generateWeirdStrips("strips", 255)
