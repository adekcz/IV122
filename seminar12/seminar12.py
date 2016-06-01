import sys, os, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parent = "/".join(cmd_folder.split("/")[0:-1])
parent += "/commonScripts"
sys.path.insert(0,parent)

import IV122Graphics
import Commons
import random



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

    def removeNeighbour(self, v):
        self.neighbours.remove(v)


    def __str__(self):
        return "{"+ str(self.data)+ ",V:"+ str(self.visited) + "}"

    def __repr__(self):
        return self.__str__()
    
def findVertexByData(maze, data):
    for vertex in maze:
        if (vertex.getData() == data):
            return vertex
    return None

def printGraph(maze, n = -1):
    if (n>0):
        for i in range(n):
            for j in range(n):
                print maze[n*i + j],
            print ""

    else:
        for vertex in maze:
            print vertex, ":[",vertex.getNeighbours() ,"]"


def generateTriangleGraph(n):
    matrix = []
    maze = []
    #generate all vertices
    for row in range(n/2+1):
        matrix.append([])
        for column in range(n-2*row):
            vertex = Vertex((column, row))
            matrix[-1].append(vertex)
            maze.append(vertex)

    #generate all edges
    for row in range(n/2+1):
        for column in range(n-2*row):
            vertexNeighbours = matrix[row][column].getNeighbours()
            if(column > 0):
                vertexNeighbours.append(matrix[row][column-1])
            if(column < len(matrix[row])-1):
                vertexNeighbours.append(matrix[row][column+1])
            if(column%2 ==0): #sudy prvek v pyramide ma souseda nad nim
                if(row>0):
                    vertexNeighbours.append(matrix[row-1][column+1])
            else: #lichy pod nim
                if(row<n-1):
                    vertexNeighbours.append(matrix[row+1][column-1])
    return maze

def drawMaze(n, maze, name ="graph"):
    
    rowCount = n/2 +1
    sizeLen = 20.0

    svg = IV122Graphics.SVG("output/" + name + ".svg" ,n*sizeLen, n*sizeLen)

    heightOfLevel = (sizeLen /2.0) * 3.0**0.5
    index = 0
    for row in range(rowCount):
        for column in range(n-2*row):
            vertex = maze[index]
            vertexNeighbours = vertex.getNeighbours()
            left = None != findVertexByData(vertexNeighbours, ( column-1, row))
            right = None != findVertexByData(vertexNeighbours, ( column+1, row))
            verticalUp = None != findVertexByData(vertexNeighbours, ( column+1, row-1))
            verticalDown = None != findVertexByData(vertexNeighbours, ( column-1, row+1))

            xoffset = row* (heightOfLevel/2)
            ycoord = heightOfLevel * row
            xcoord = xoffset +  sizeLen* ((column+1)//2)

            print vertex,vertexNeighbours, left, right, verticalUp, verticalDown, xcoord, ycoord
            if(column %2 == 0): #spicka dole
                if(verticalUp):
                    svg.line(xcoord, ycoord, xcoord+sizeLen, ycoord)
                if(right):
                    svg.line(xcoord+sizeLen, ycoord, xcoord+(sizeLen/2), ycoord+heightOfLevel)
                if(left):
                    svg.line(xcoord+(sizeLen/2), ycoord+heightOfLevel,xcoord, ycoord)
            else:
                if(right):
                    svg.line(xcoord, ycoord, xcoord+sizeLen/2, ycoord+heightOfLevel)
                if(verticalDown):
                    svg.line(xcoord+sizeLen/2, ycoord+heightOfLevel,xcoord-sizeLen/2, ycoord+heightOfLevel)
                if(left):
                    svg.line(xcoord-sizeLen/2, ycoord+heightOfLevel,xcoord, ycoord)

            index = index+1

        print 



#vnejsi strany
    svg.line(0, 0, sizeLen*rowCount, 0)
    svg.line(sizeLen*rowCount, 0, sizeLen*rowCount/2.0, rowCount*heightOfLevel)
    svg.line( sizeLen*rowCount/2.0, rowCount*heightOfLevel,0, 0)
    svg.line

    svg.close()




def generateRandomMaze(maze, n, vertex):

    vertex.setVisited()
    neighbours = vertex.getNeighbours()


    copyForTraversal = neighbours[:]
    random.shuffle(copyForTraversal)

    print vertex,neighbours
    for neighbour in copyForTraversal:
        print "\t", neighbour
        if (not neighbour.getVisited()):
            neighbour.setVisited()
            vertex.removeNeighbour(neighbour)
            neighbour.removeNeighbour(vertex)
            generateRandomMaze(maze, n, neighbour)


if __name__ == "__main__":
    n = 5
    maze = generateTriangleGraph(n)
    drawMaze(n, maze, "one")
    generateRandomMaze(maze, n, maze[0])
    drawMaze(n, maze, "generatedone")
    print "-------------"
    n = 19
    maze = generateTriangleGraph(n)
    drawMaze(n, maze, "two")
    print "starting dfs"
    generateRandomMaze(maze, n, maze[0])
    print "finished dfs"
    drawMaze(n, maze, "generatedtwo")
