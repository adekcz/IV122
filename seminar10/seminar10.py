import sys, os, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parent = "/".join(cmd_folder.split("/")[0:-1])
parent += "/commonScripts"
sys.path.insert(0,parent)

import random
import IV122Graphics
import Commons

def drawAxes(size, svg):
    #svg.line(size/2, 0, size/2, size)
    #svg.line(0, size/2, size, size/2)

    svg.line(-size/2, 0, size/2, 0)
    svg.line(0, -size/2, 0, size/2)

def computeLine(data):
    sumX = 0
    sumY = 0
    sumXY = 0
    sumXSquared = 0
    n = len(data)
    for point in data:
        x = point[0]
        y = point[1]

        sumX = sumX + x
        sumY = sumY + y
        sumXY = sumXY + x * y
        sumXSquared = sumXSquared + x*x

    a =  float(n*sumXY - sumX*sumY)/(n*sumXSquared-sumX*sumX)
    b = float(sumY)/n - a*float(sumX)/n

    return (a,b)


def computeSSE(data, line):
    SSE = 0
    for point in data:
        SSE = SSE + (point[1] - line(point[0]))**2

def linearRegression(inFile, outFile):

    inputData = open(inFile)
    points = [(float(line.split(" ")[0]), float(line.split(" ")[1])) for line in inputData.readlines()]
    size = 200

    svg = IV122Graphics.SVG("output/" + outFile + ".svg" ,size, size)
    svg.resizeCoordinates(16,16)
    svg.flipByX()
    svg.setMidInCenter()
    drawAxes(size, svg)

    analyticalLinRegression(points, svg)
    gridSearchLinRegression(points,svg)


    svg.close()


def drawComputedLine(a,b, svg, color):
    lineY = lambda a,b,x: a*x +b

    x1=-5
    x2= 5

    svg.setStroke(color)
    lineY = lambda x: a*x +b
    svg.line(x1, lineY(x1), x2, lineY(x2))
    svg.setStroke("black")

def gridSearchLinRegression(points, svg):
    minSSE = 12345678
    (minA,minB) = (0,0)

    for a in range(20,30):
        for b in range(10,20):
            fa = float(a)/10
            fb = float(b)/10

            sse = computeSSE(points, lambda x: x*fa  + fb)
            if (sse < minSSE):
                minSSE = sse
                (minA,minB) = (fa,fb)

    drawComputedLine(minA, minB, svg, "blue")



def analyticalLinRegression(points, svg):
    
    for point in points:
        svg.circle(1, point[0] , point[1] )

    (a,b) = computeLine(points)

    drawComputedLine(a,b, svg, "red")


def getRandomPointInInterval(minX, maxX, minY, maxY):

    return (minX + random.random()*abs(maxX-minX),minY + random.random()*abs(maxY-minY))


def dist(a,b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

def findNearestCluster(point, centers):
    minDist = 0
    closestCenter = -1
    for i in range(len(centers)):
        curDist = dist(centers[i], point)
        if(minDist>curDist or closestCenter == -1):
            minDist = curDist
            closestCenter = i
        
    return closestCenter   

def computeCenters(clusters):
    centers = [] 
    for cluster in clusters:
        xs = [p[0] for p in cluster]
        ys = [p[1] for p in cluster]
        n = len(clusters)

        centers.append((float(sum(xs))/n, float(sum(ys))/n))
    return centers

    
def kmeans(inFile, k, outFile):
    inputData = open(inFile)
    points = [(float(line.split(" ")[0]), float(line.split(" ")[1])) for line in inputData.readlines()]

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    minX = min(xs)
    maxX = max(xs)
    minY = min(ys)
    maxY = max(ys)

    print (minX, maxX, minY, maxY)
    centers = [getRandomPointInInterval(minX, maxX, minY, maxY) for x in range(k)]
    print "Centers original: ", centers
    clusters = [[] for x in range(k)]

    for i in range(30):
        for point in points:
            clusters[findNearestCluster(point, centers)].append(point)
        for j in range(len(clusters)):
            print "cluster: ",j, clusters[j]
        drawClusters("step"+str(i),minX, maxX, minY, maxY, points, centers)
        centers = computeCenters(clusters)
        print "Centers, cont: ", centers
        clusters = [[] for x in range(k)]


    drawClusters("final",minX, maxX, minY, maxY, points, centers)
    

def drawClusters(name, minX, maxX, minY, maxY, points, centers):
    size = 200
    svg = IV122Graphics.SVG("output/" + name + ".svg" ,size, size)
    imgMaxCoord = 2* max([minX, maxX, minY, maxY]) #vsechny body se musi vlezt do obrazku, pulka je uprostred, takze *2
    svg.resizeCoordinates(imgMaxCoord,imgMaxCoord)
    svg.flipByX()
    svg.setMidInCenter()
    drawAxes(size, svg)

    colors = ["black", "red", "blue", "green", "yellow", "orange", "purple", "grey"] #obviously, limited to 9 clusters
    for point in points:
        cluster = findNearestCluster(point, centers)
        print cluster, colors[cluster]
        svg.setFill(colors[cluster])
        svg.setStroke(colors[cluster])
        svg.circle(1, point[0], point[1])

    svg.close()
    
def generateClusterFile(k, name):
    centers = [ getRandomPointInInterval(-1, 1, -1, 1) for x in range(k)]
    
    print centers

    f = open(name, "w")
    for i in range(100):
        curPooint = (centers[i%k][0] + random.random()/10, centers[i%k][1] + random.random()/10)
        f.write(str(curPooint[0]) + " " + str(curPooint[1]) +"\n" )
    f.close()   

if __name__ == "__main__":
    #linearRegression("linreg.txt", "linreg")
    name = "clusters.txt"
    #generateClusterFile(3,name)
    kmeans("clustersNice.txt", 8, "clusters")
