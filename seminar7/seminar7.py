import sys, os, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parent = "/".join(cmd_folder.split("/")[0:-1])
parent += "/commonScripts"
sys.path.insert(0,parent)

import IV122Graphics
import Commons

def nextMandelBrot(curr, c):
    return curr*curr + c
    

#-2.0 <= cutX, cutY <=2.0
def mandelBrot(imgSize, cutX, cutY, cutSize, name = "mandelbrot"):
#imgsize resaclovat na ctverec -2, 2
    #cutX = -1
    #cutY = -1
    #cutSize = imgSize/4.0

#multiply something by cutSize, add cutX to something, add cutY to something

    scaleFactor = imgSize / (4.0 )
    scaleFactor2 = imgSize / cutSize
    #scaleFactorX = imgSize / (4.0 * (-2.0/cutX)) #
    #scaleFactorY = imgSize / (4.0 * (-2.0/cutY)) # bullshit

# scaledX cutX
#         -2   = 0
#         -1   = +1
#          0     +2 
#          1     +3
#          2     +4 

    depth = 20
    simpleHeuristic = 2

    bitmap = IV122Graphics.BitMap("output/" + name + ".jpg", imgSize, imgSize)

    for x in range(-imgSize/2, imgSize/2):
        for y in range(-imgSize/2, imgSize/2):
            z = complex(0,0)
            scaledX = x/scaleFactor 
            scaledY = y/scaleFactor
            c = complex((scaledX/scaleFactor2) + cutX - 2, (scaledY/scaleFactor2) + cutY - 2 )
            currDepth = 0
            while abs(z) < simpleHeuristic and currDepth < depth:
                z = nextMandelBrot(z, c)
                currDepth+=1


            if abs(z) < simpleHeuristic:
                distane = abs(z)
                color = ((255.0* distane) / simpleHeuristic)
                bitmap.putPixel(x+imgSize/2, y+imgSize/2, (color,0,0))
            else:
                color = ((255.0* currDepth) / depth)
                bitmap.putPixel(x+imgSize/2, y+imgSize/2, (0,color,0))

    bitmap.close()

    
def juliusSet():
    imgSize = 400
    depth = 20
    simpleHeuristic = 2

    bitmap = IV122Graphics.BitMap("output/julii.jpg", imgSize, imgSize)

    for x in range(-imgSize/2, imgSize/2):
        for y in range(-imgSize/2, imgSize/2):
            z = complex(x/100.0,y/100.0)
            c = complex(-0.13,0.75) 
            currDepth = 0
            while abs(z) < simpleHeuristic and currDepth < depth:
                z = nextMandelBrot(z, c)
                currDepth+=1


            if abs(z) < simpleHeuristic:
                distane = abs(z)
                color = ((255.0* distane) / simpleHeuristic)
                bitmap.putPixel(x+imgSize/2, y+imgSize/2, (color,0,0))
            else:
                color = ((255.0* currDepth) / depth)
                bitmap.putPixel(x+imgSize/2, y+imgSize/2, (0,color,0))

    bitmap.close()


if __name__ == "__main__":
    imgSize = 1600
    mandelBrot(imgSize, -1, -1, 400, "mandelBrot_1_1")
    mandelBrot(imgSize, -1, 0, 400, "mandelBrot_10")
    mandelBrot(imgSize, 0, 1, 400, "mandelBrot01")
    juliusSet()

    bitmap = IV122Graphics.BitMap("output/test.jpg", 400, 400)
    bitmap.close()

