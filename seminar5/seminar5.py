import sys, os, inspect
import random
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parent = "/".join(cmd_folder.split("/")[0:-1])
parent += "/commonScripts"
sys.path.insert(0,parent)

import IV122Graphics
import Commons
import math




def intersections(n, name, normal = False):
    size = 400
    img = IV122Graphics.SVG("output/" + name + ".svg", size, size)

    lines = generateLineSegments(n, size, normal)
    img.setFill()

    for line in lines:
        img.line(line[0][0],line[0][1],line[1][0], line[1][1])
        
    for line1 in lines:
        for line2 in lines:
            if(line1 != line2):
                inter = Commons.computeLineIntersection(line1[0], line1[1], line2[0], line2[1])
                if (inter == -1):
                    continue
                img.setFill("Red")
                img.circle(3, inter[0], inter[1])
                img.setFill()



    img.close()

def closure(n):
    size = 400
    img = IV122Graphics.SVG("output/closure.svg", size, size)

    points = generatePoints(n, size)
    img.setFill()

    for p in points:
        img.circle(5, p[0], p[1])
        
    
    while(len(points)>0):
        startPoint = leftMostPoint(points)
        img.setFill("Blue")
        img.circle(10, startPoint[0], startPoint[1])
        img.setFill()

#doprav adolu
        cond = lambda startPoint, point: (point[0]>startPoint[0] and point[1]>startPoint[1])
        computation = lambda startPoint, point:  float(point[0] - startPoint[0]) / float((point[1]- startPoint[1]))

        startPoint =  partialConvexClosure(startPoint, points, cond, computation, img)
                        
#doprava nahoru
        cond = lambda startPoint, point: (point[0]>startPoint[0] and point[1]<startPoint[1])
        computation = lambda startPoint, point:   float( startPoint[1]- point[1])/float(point[0] - startPoint[0]) 

        startPoint =  partialConvexClosure(startPoint, points, cond, computation, img)
                        
#doleva nahoru
        cond = lambda startPoint, point: (point[0]<startPoint[0] and point[1]<startPoint[1])
        computation = lambda startPoint, point:   float( startPoint[0]- point[0])/float(startPoint[1] - point[1]) 
        startPoint =  partialConvexClosure(startPoint, points, cond, computation, img)

#doleva dolu
        cond = lambda startPoint, point:  (point[0]<startPoint[0] and point[1]>startPoint[1])
        computation = lambda startPoint, point:   float( point[1]- startPoint[1])/float(startPoint[0] - point[0]) 
        startPoint =  partialConvexClosure(startPoint, points, cond, computation, img)

    img.close()

def vectorSize(a, b):
    return math.sqrt(a**2 + b**2)
    
def partialConvexClosure(startPoint, points, condition, ratioComputation, img):
    minPoint = startPoint
    for j in range(len(points)):
        minRatio = 100000
        minPoint = startPoint
        for i in range(len(points)):
            point = points[i]
            if (condition(startPoint, point)):
                ratio = ratioComputation(startPoint, point) #tangens pomer..
                if (ratio<minRatio):
                    minPoint = point
                    minRatio = ratio
        
        img.line(startPoint[0], startPoint[1],minPoint[0],minPoint[1])
        startPoint = minPoint
        if minPoint in points: points.remove(minPoint)
    return minPoint

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

def generatePoints(n,upperLimitForCoordinate,  normal = False):
    result = []
    for i in range(n):
        if (normal):
            result.append((random.normalvariate(upperLimitForCoordinate/2,upperLimitForCoordinate/(4)), random.normalvariate(upperLimitForCoordinate/2,upperLimitForCoordinate/(4)) ))
        else:
            result.append((random.uniform(0, upperLimitForCoordinate), random.uniform(0, upperLimitForCoordinate)))
    
    return result

def generateLineSegments(n, upperLimitForCoordinate, normal = False):
    points = generatePoints(n*2, upperLimitForCoordinate, normal)
    resultLineSegments = []
    for i in range(n):
        resultLineSegments.append((points[i*2], points[i*2 +1]))
    return resultLineSegments



if __name__ == "__main__":
    n = 20
    #intersections(20, "intersectionsUniform1")
    #intersections(20, "intersectionsUniform2")
    #intersections(20, "intersectionsNormalDist1", True)
    #intersections(20, "intersectionsNormalDist2", True)
    closure(40)
    print(Commons.radToDeg(math.atan(1)))

