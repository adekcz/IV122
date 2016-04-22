import sys, os, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parent = "/".join(cmd_folder.split("/")[0:-1])
parent += "/commonScripts"
sys.path.insert(0,parent)


import IV122Graphics
import Commons
import math
import copy


def matrixProduct(matA, matB):
    #print("A:")
    #Commons.printArray(matA)
    #print("B:")
    #Commons.printArray(matB)
    cols_count = len(matB[0])
    rows_count = len(matA[0])
    resultMat = [[0 for x in range(cols_count)] for x in range(rows_count)]

    for x in range(cols_count):
        for y in range(rows_count):
            for i in range(rows_count):
                resultMat[y][x] += matA[y][i] *  matB[i][x]
    return resultMat

def rotateMat(angle):
    alfaInRad = Commons.degToRad(angle)
    return [[math.cos(alfaInRad), -math.sin(alfaInRad), 0], [math.sin(alfaInRad),math.cos(alfaInRad),0], [0,0,1]]

def rotate(mat, angle):
    return matrixProduct(rotateMat(angle), mat)

def translateMat(x, y):
    return [[1,0,x], [0, 1, y], [0,0,1]]

def translate(mat, x, y):
    return matrixProduct(translateMat(x, y), mat) 

def scalingMat(dx, dy):
    return [[dx,0,0], [0, dy, 0], [0,0,1]]

def scaling(mat, dx, dy):
    return matrixProduct(scalingMat(dx, dy), mat) 

def shearMat(k):
    return [[1,k,0], [0, 1, 0], [0,0,1]]

def shear(mat, k):
    return matrixProduct(shearMat(k), mat) 

def transposeVec(vec):
    result = []
    for i in range(vec):
        result.append([i])

def getFirstImage(imgSize):

    points= [[[0],[0], [1]],[[0],[imgSize], [1]],[[imgSize],[imgSize], [1]],[[imgSize],[0], [1]]]
    result = []
    for i in range(len(points)):
        result.append([points[i], points[(i+1) % len(points)]])
    return result

def applyTransformations(lineSegments, transformations, count = 1):
    resultList = []
    for i in range(len(lineSegments)): 
        # lineSegments to points, and back to lineSegments
        newPoints = []
        for point in  lineSegments[i]:
            newPoints.append(matrixProduct(transformations, point))
        resultList.append(newPoints) 

    return resultList

def drawImage(lineSegments, name):
    dim = 1600
    svg = IV122Graphics.SVG("output/" + name + ".svg" ,dim, dim)
    #print lineSegments
    for line in lineSegments:
        svg.line(line[0][0][0] + dim/2, line[0][1][0] + dim/2, line[1][0][0] + dim/2, line[1][1][0] + dim/2)
    svg.close()

def applyNTimes(transformation,  n, origImage, keepOririgin = True):
    if (keepOririgin):
        resultLines = copy.deepcopy(origImage)
    else:
        resultLines = []
    lastResult = copy.deepcopy(origImage)
    for i in range(n):
        #print("I: " + str(i) + " " + str(lastResult))
        lastResult = applyTransformations(lastResult, transformation)
        resultLines.extend(lastResult)
    return resultLines

def sample1():
    transformation = matrixProduct(matrixProduct(rotateMat(20), scalingMat(1.1, 1.1)), translateMat(5,10))
    origImage = getFirstImage(40)
    print("0")
    Commons.printArray(origImage)
    resultLines = applyNTimes(transformation, 10, origImage)
    print("1")
    Commons.printArray(origImage)
    drawImage(resultLines, "rectangle") 
    transformation =  shearMat(1.2)
    resultLines = applyNTimes(transformation, 10, origImage)
    print("2")
    Commons.printArray(origImage)
    drawImage(resultLines, "shear") 
    transformation =  scalingMat(2, 3)
    resultLines = applyNTimes(transformation, 10, origImage)
    drawImage(resultLines, "scale") #OK
    transformation =  rotateMat(20)
    resultLines = applyNTimes(transformation, 10, origImage)
    drawImage(resultLines, "rotate") 
    transformation =  translateMat(20, 5)
    #Commons.printArray(transformation)
    resultLines = applyNTimes(transformation, 1, origImage)
    #Commons.printArray(resultLines)
    drawImage(resultLines, "translate") 

    transformation = matrixProduct(rotateMat(10), scalingMat(1.1, 0.8))
    resultLines = applyNTimes(transformation, 15, origImage)
    drawImage(resultLines, "sample2") 

    transformation = matrixProduct(matrixProduct(matrixProduct(shearMat(1.3), rotateMat(10)), scalingMat(0.9, 0.9)), translateMat(10, 10))
    resultLines = applyNTimes(transformation,  25, origImage)
    drawImage(resultLines, "sample3") 
#Repeat 25: shear(1.3), rotation(10), scaling(0.9,0.9), translation(50, 50)

def printMatrixesOfLines(data):
    for i in range(len(data)):
        print("i: " + str(i))
        Commons.printArray(data[i])
#multiple reduction copy machine
def mrcm(matrices,  nesting = 5):
    current = getFirstImage(200)
    tempCurrent = []
    for i in range(nesting):
        print(i)
        for matrix  in matrices:
            #Commons.printArray(matrix)
            tempCurrent.extend(applyNTimes(matrix, 1, current, False))
            printMatrixesOfLines(tempCurrent)
            print("\n")
        current = tempCurrent
        tempCurrent = []
    return current

def testingMrcmStar():
    origImage = getFirstImage(200)
    transformation = [[0.255, 0, 0.3726],[0, 0.255, 0.6714], [0,0,1]]
    resultLines = applyNTimes(transformation, 1, origImage)
    printMatrixesOfLines(resultLines)
    drawImage(resultLines, "mrcmStarStep1") 

def mrcmStar():
    matrices = [[[0.255, 0, 0.3726*200],[0, 0.255, 0.6714*200], [0,0,1]],
                [[0.255, 0, 0.1146*200],[0, 0.255, 0.2232*200], [0,0,1]],
                [[0.255, 0, 0.6306*200],[0, 0.255, 0.2232*200], [0,0,1]],
                [[0.37, -0.642, 0.6356*200],[0.642, 0.37, -0.0061*200], [0,0,1]]]
    lines = mrcm(matrices, 4)
    drawImage(lines, "mrcmStar")

if __name__ == "__main__":
    print("neco")

    #sample1()

    mrcmStar()

    #testingMrcmStar()

