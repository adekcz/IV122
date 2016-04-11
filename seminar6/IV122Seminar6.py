import sys, os, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parent = "/".join(cmd_folder.split("/")[0:-1])
parent += "/commonScripts"
sys.path.insert(0,parent)

import IV122Graphics
import Commons
import random, math

def getRandomPoint(size):
    return (random.random() * size, random.random() * size)

#put into commons
def generateNGonPoint(n, size):
    result = []
    for i in range(n):
        result.append((math.cos(Commons.degToRad(i* 360/n)), math.sin(Commons.degToRad(i* 360/n))))
    for i in range(n):
        result[i] = (result[i][0]* (size/2) +size/2, result[i][1]* (size/2) +size/2)
    return result
    
def computeMidPoint(a, b, ratio=0.5):
    return ((a[0] + b[0])*ratio, (a[1] + b[1])*ratio)


def chaosgame(path, ngon, ratio):
    imgSize = 800
    jpeg = IV122Graphics.BitMap(path, imgSize,imgSize)
    outerPoints = generateNGonPoint(ngon, imgSize/ngon)

    stepCount = 10000

    point  = getRandomPoint(imgSize)
    for i in range(stepCount):
        chosenOrigin = random.randint(0, ngon-1)
        point = computeMidPoint(outerPoints[chosenOrigin], point, ratio)
        if(i>100):
            jpeg.putPixel(point[0],point[1], (255, 0, 0))
    jpeg.close()


def parallelRewrite(inputString, rules):
    result = ""
    for c in inputString:
        for rule in rules:
            if c == rule[0]:
                result += rule[1]
            else:
                result += c
    return result

def drawImage(name, inputString, rulesInterpretation):
    size = 800
    turtle = IV122Graphics.Turtle(name,  size, size, 20, size*3/4)
    for c in inputString:
        eval("turtle." + rulesInterpretation[c])
    turtle.close()
    
        
def LSystemGenerator(name, init, rules, interpretation, nesting):
    tempString = init
    for i in range(nesting):
        tempString = parallelRewrite(tempString, rules)
        

    drawImage(name, tempString, interpretation)
    return

if __name__ == "__main__":
    #print(generateNGonPoint(3,100))
    #chaosgame("output/chaos3_half.jpg", 3, 0.5)
    #chaosgame("output/chaos5_third.jpg", 5, 1.0/3)
    #chaosgame("output/chaos6_third.jpg", 6, 1.0/3)

    
    LSystemGenerator("output/lsystem1.svg", "F--F--F", [("F", "F+F--F+F")], 
    {"F" : "forward(2)", "+" : "right(60)", "-" : "left(60)"}, 5)
