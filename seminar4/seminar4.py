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
            halfplane2 = i_y <= -math.sqrt(3.0)/2 * i_x + math.sqrt(3.0)*size/2
            halfplane3 = i_y <= math.sqrt(3.0)/2 * i_x + -math.sqrt(3.0)*size/2

            if (halfplane1 and halfplane2 and halfplane3):
                bitmap.putPixel(i_x, i_y, (100, 100, 100))
    bitmap.close()

def drawFilledPolygon(points,name,  size):
    bitmap = IV122Graphics.BitMap("output/" + name + ".jpg", size, size)

    bitmap.close()


if __name__ == "__main__":
    circle("empty", 150,250,50, 0)
    circle("full", 150,250,50, 1)
    spiral("spiral", 250,250,50)
    colorEquilateralTriangle("triangle")
    drawFilledPolygon( [(10, 10), (180, 20), (160, 150), (100, 50), (20, 180)],"polygon",  400)

