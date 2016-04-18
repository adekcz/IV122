import sys, os, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parent = "/".join(cmd_folder.split("/")[0:-1])
parent += "/commonScripts"
sys.path.insert(0,parent)


import IV122Graphics
import Commons


def matrixProduct(matA, matB):
    cols_count = len(matB[0])
    rows_count = len(matA[0])
    resultMat = [[0 for x in range(cols_count)] for x in range(rows_count)]

    for x in range(cols_count):
        for y in range(rows_count):
            for i in range(cols_count):
                resultMat[y][x] += matA[y][i] *  matB[i][x]
    return resultMat

def rotate(mat, angle):
    alfaInRad = Commons.degToRad(angle)
    return matrixProduct([[math.cos(alfaInRad), -math.sin(alfaInRad), 0], [math.sin(alfaInRad),math.cos(alfaInRad),0], [0,0,1]], mat)

def translate(mat, x, y):
    return matrixProduct([[1,0,x], [0, 1, y], [0,0,1]], mat) 

def scaling(mat, dx, dy):
    return matrixProduct([[dx,0,0], [0, dy, 0], [0,0,1]], mat) 

def shear(mat, k):
    return matrixProduct([[1,k,0], [0, 1, 0], [0,0,1]], mat) 

def getFirstImage():
    points= [[0,0],[0,1],[1,1],[1,0]]
    result = []
    for i in range(len(points)-1):
        result.append([points[i], points[i+1]])


def drawImage(lineSegments, name):
    dim = 600
    svg = IV122Graphics.SVG("output/" + name + ".svg" ,dim, dim)
    for line in lineSegments:
        svg.line(line[0], line[1])
    svg.close()

if __name__ == "__main__":
    #Commons.printArray(matrixProduct([[2,-0.5],[-0.5, 3]],[[3],[2]]))
    Commons.printArray(getFirstImage())
