import sys, os, inspect
import random
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parent = "/".join(cmd_folder.split("/")[0:-1])
parent += "/commonScripts"
sys.path.insert(0,parent)

import IV122Graphics
import Commons
import math




def closure(n):
    size = 400
    img = IV122Graphics.SVG("output/closure.svg", size, size)

    points = generatePoint(n, size)
    img.setFill()

    for p in points:
        img.circle(5, p[0], p[1])
        
    startPoint = leftMostPoint(points)
    img.setFill("Red")
    img.circle(10, startPoint[0], startPoint[1])
    img.setFill()
    currentPoint = startPoint

    for i in range(len(points)):
        nextPoint = findNextPointUniversal(currentPoint, points, lambda origin,p: p[0] < origin[0] or p[1]<origin[1], lambda origin, p: float(p[0] - origin[0]) / float(p[1]- origin[1]))
        img.line(currentPoint[0], currentPoint[1],nextPoint[0],nextPoint[1])
        currentPoint = nextPoint
    for i in range(len(points)):
        nextPoint = findNextPointUniversal(currentPoint, points, lambda origin,p: p[0] < origin[0] or p[1]>origin[1], lambda origin, p: float(abs(p[1] - origin[1])) / float(abs(p[0]- origin[0])))
        img.line(currentPoint[0], currentPoint[1],nextPoint[0],nextPoint[1])
        currentPoint = nextPoint


    img.close()

def vectorSize(a, b):
    return math.sqrt(a**2 + b**2)
    
def findNextPointUniversal(origin, points, condition, ratioComputation):
    largestSoFar = 100
    result = origin
    for p in points:
        if(p == origin):
            continue
        if(condition(origin, p)):
            continue
        ratio = ratioComputation(origin, p)
        newAngle = Commons.radToDeg(math.atan(ratio))
        if newAngle < largestSoFar: #todo change variable to smallest
            result = p
            largestSoFar = newAngle
    #print()
    return result

def findNextPointRightLower(origin, points):
    largestSoFar = 100
    result = origin
    for p in points:
        if(p == origin):
            continue
        if(p[0] < origin[0] or p[1]<origin[1]):
            continue
        ratio = float(p[0] - origin[0]) / float(p[1]- origin[1])
        newAngle = Commons.radToDeg(math.atan(ratio))
        if newAngle < largestSoFar: #todo change variable to smallest
            result = p
            largestSoFar = newAngle
    #print()
    return result

def findNextPointRightUpper(origin, points):
    largestSoFar = 100
    result = origin
    for p in points:
        if(p == origin):
            continue
        if(p[0] < origin[0] or p[1]>origin[1]):
            continue
        ratio = float(abs(p[1] - origin[1])) / float(abs(p[0]- origin[0]))
        newAngle = Commons.radToDeg(math.atan(ratio))
        if newAngle < largestSoFar: #todo change variable to smallest
            result = p
            largestSoFar = newAngle
    #print()
    return result

def leftMostPoint(points):
    result = points[0]
    for p in points:
        if p[0]<result[0]:
            result = p
    return result

def generatePoint(n,upperLimit,  normal = False):
    result = []
    for i in range(n):
        if (normal):
            result.append((random.normalvariate(upperLimit/2,upperLimit/(6*2)), random.normalvariate(upperLimit/2,upperLimit/(6*2)) ))
        else:
            result.append((random.uniform(0, upperLimit), random.uniform(0, upperLimit)))
    
    return result

if __name__ == "__main__":
    n = 20
    closure(40)
    print(Commons.radToDeg(math.atan(1)))

