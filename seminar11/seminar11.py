import sys, os, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parent = "/".join(cmd_folder.split("/")[0:-1])
parent += "/commonScripts"
sys.path.insert(0,parent)

import IV122Graphics
import Commons

class Vertex:
    def __init__(self, data, visited=False):
        self.data = data
        self.visited =visited
        self.neighbours = []

    def addNeighbour(self, v):
        self.neighbours.append(v)

    def getNeighbours(self):
        return self.neighbours

    def getData(self):
        return self.data

    def getVisited(self):
        return self.visited

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return "{"+ str(self.data)+ ",V:"+ str(self.visited) + "}"

    def __repr__(self):
        return self.__str__()
    

def nummazefinish(vertex, graph):
    if (vertex == graph[-1]):
        return True
    return False

def robotMazeFinish(vertex, graph):
    return vertex.getData()[3]


#zjistit jednoznacost: najit delku cesty k nejkratsimu reseni. Dokoncit aktualne prohledavanou uroven hloubky. Behem pruchodu si znacit, v jake urovni byl uzel navstiven. Pakj jit po zpetnych hranach od cile. 
#pokud najdu uzel, ve kterem vedou dve hrany do  uzlu s nizsi poznacenou urovni, znamena to, ze tam bude vice cest..
def bfs(graph, start,finishCondition):


    firstSolutionFoundOnLevel = -1

    start.setVisited()
    queue = [(start, 0)] #(vertex, level in which it was transitioned)
    while(queue):
        #print("-")
        #printGraph(graph)
        (vertex, level) = queue.pop(0)

        if (firstSolutionFoundOnLevel == level):
            if(finishCondition(vertex, graph)):
                print "Nalezena dalsi cesta nahodou"
            continue #urcite uz nepridavat dalsi hrany

        #    continue #urcite nepridavat dalsi do fronty
        if (finishCondition(vertex, graph)):
            print "Nalezena cesta", vertex
            printGraph(maze, 4)
            firstSolutionFoundOnLevel = level
            continue
        
        neighbours =  vertex.getNeighbours()
        #print neighbours

        for neighbour in neighbours:
            #print("in for", vertexCoord, " ", vertex1.getData(), " ", vertex1.getVisited())
            if (not neighbour.getVisited()):
                neighbour.setVisited()
                queue.append( (neighbour, level +1))
        #print queue
    
def printMatrix(maze):
    width = len(maze[0])
    height = len(maze)
    for line in maze:
        for value in line:
            print value,
        print()

def printGraph(maze, n = -1):
    if (n>0):
        for i in range(n):
            for j in range(n):
                print maze[n*i + j],
            print ""

    else:
        for vertex in maze:
            print vertex, ":[",vertex.getNeighbours() ,"]"


def getNeighbours(maze,x,y):
    number = maze[y][x]
    width = len(maze[0])
    height = len(maze)

    neighbours = []
    if (x+number < width):
        neighbours.append((x+number, y))
    if (x-number >= 0):
        neighbours.append((x-number, y))
    if (y+number < height):
        neighbours.append((x, y+number))
    if (y-number >= 0):
        neighbours.append((x, y-number))


    return neighbours

def loadNumericalMaze(path):
    mazeInFile = open(path)
    mazeAsMatrix = []
    mazeAsMatrixOfVertices = []
    graph = []
    
    x = 0
    y= 0
    for line in mazeInFile.readlines():
        mazeAsMatrix.append([])
        mazeAsMatrixOfVertices.append([])

        for strNum in line.split(" "):
            mazeAsMatrix[-1].append(int(strNum))
            vertex = Vertex((x,y,int(strNum)))
            mazeAsMatrixOfVertices[-1].append(vertex)
            graph.append(vertex)
            x = x +1
        y = y+1
        x = 0
    
    printMatrix(mazeAsMatrix)
    printGraph(graph)

    #pridej sousedy uzlum
    width = len(mazeAsMatrix[0])
    height = len(mazeAsMatrix)
    for y in range(height):
        for x in range(width):
            print x, y
            neighbours = getNeighbours(mazeAsMatrix, x, y)
            neighbousOfVertex = mazeAsMatrixOfVertices[y][x].getNeighbours()
            for neighbour in  neighbours:
                neighbousOfVertex.append(mazeAsMatrixOfVertices[neighbour[1]][neighbour[0]])
    printGraph(graph)
    return graph

def findVertexByData(maze, data):
    for vertex in maze:
        if (vertex.getData() == data):
            return vertex
    return None

def getNextVertex(maze, current):
    deltas = [(1,0), (0,-1), (-1,0), (0,1)]
    data = current.getData()
    delta = deltas[data[2]]
    notGoal = findVertexByData(maze, (data[0]+delta[0], data[1] + delta[1], data[2], False))
    if(notGoal):
        return notGoal
    return  findVertexByData(maze, (data[0]+delta[0], data[1] + delta[1], data[2], True))

def loadRobotInMaze(path):
    mazeInFile = open(path)
    mazeAsMatrixOfVertices = []
    graph = []
    
    x = 0
    y= 0

    print "vytvor uzly"
#vytvor vsechny uzly (x,y, orientation, isgoal)
    for line in mazeInFile.readlines():
        for char in line[:-1]: #omit \n
            if (char == "o"):
                for i in range(4):
                    vertex = Vertex((x,y,i, False))
                    graph.append(vertex)
            if (char == "G"):
                for i in range(4):
                    vertex = Vertex((x,y,i, True))
                    graph.append(vertex)
            x = x +1
        y = y+1
        x = 0
#vytvor hrany 
    printGraph(graph)
    print "vytvor hrany"
    for vertex in graph:
        nextVertex = getNextVertex(graph, vertex)
        if(nextVertex):
            vertex.getNeighbours().append(nextVertex)
        data = vertex.getData()
        vertex.getNeighbours().append(findVertexByData(graph, (data[0], data[1], (data[2]+1)%4, data[3])))
        vertex.getNeighbours().append(findVertexByData(graph, (data[0], data[1], (data[2]-1)%4, data[3])))


    printGraph(graph)
    return graph

if __name__ == "__main__":
    #maze = loadNumericalMaze("maze1Num.txt")
    print "bfs:"
    #bfs(maze,maze[0], numMazeFinish)
    maze = loadRobotInMaze("robotInMaze1.txt")
    bfs(maze, maze[0], robotMazeFinish)

#1. BFS
#2. dijkstra
#3. DFS 
#4. NP?
#5. NP?
#6. takove ty hladove, jarnici, boruvky...



