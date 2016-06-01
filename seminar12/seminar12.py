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
    for row in range(n):
            matrix.append([])
        for column in range(len(n-row)):
            vertex = Vertex((column, row))
            matrix[-1].append(vertex)
            maze.append(vertex)

    #generate all edges
    for row in range(len(n)):
        for column in range(len(n-row)):
            vertexNeighbours = matrix[row][column].getNeighbours()
            if(column > 0):
                vertexNeighbours.append(matrix[row][column-1])
            if(column < len(matrix[row])-1):
                vertexNeighbours.append(matrix[row][column+1])
            if(column%2 ==0): #sudy prvek v pyramide ma souseda nad nim
                if(row<n-1):
                    vertexNeighbours.append(matrix[row-1][column+1])
            else: #lichy pod nim
                if(row>0):
                    vertexNeighbours.append(matrix[row+1][column-1])




if __name__ == "__main__":
