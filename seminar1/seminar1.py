import sys, os, inspect
#hack to allow importing from specific directory
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parent = "/".join(cmd_folder.split("/")[0:-1])
parent += "/commonScripts"
sys.path.insert(0,parent)

import IV122Graphics
import Commons

def squaredRainbow():
    ff = 255
    bitmap = IV122Graphics.BitMap("output/squaredRainbow.jpg", ff, ff)
    for i in range(ff):
        for j in range(ff):
            bitmap.putPixel(i, j, (i,j,ff))
    bitmap.close()

def weirdGrid():
    dim = 400
    stepSize = 20
    svg = IV122Graphics.SVG("output/curvyGrid.svg" ,dim, dim)
    coords = ((0, 1, 1), (0, 1, -1), (1, -1, 1), (1, -1, -1))

    for quadrant in range(4):
        for i in range(11):
            svg.line((dim*coords[quadrant][0]) + coords[quadrant][1]*stepSize*i ,dim/2,dim/2 , dim/2 + coords[quadrant][2]* stepSize*i)

    #naive
    #for i in range(11):
        #svg.line(stepSize*i ,dim/2,dim/2 , dim/2 - stepSize*i)
    #for i in range(11):
        #svg.line(dim - stepSize*i ,dim/2,dim/2 , dim/2 + stepSize*i)
    #for i in range(11):
        #svg.line(dim - stepSize*i ,dim/2,dim/2 , dim/2 - stepSize*i)
    #for i in range(11):
        #svg.line(dim/2 ,stepSize*i,dim/2 - stepSize*i , dim/2)
    svg.close()

def collatz(n):
    #print(str(n) + " " , end="")
    if(n==1):
        return 0
    if (n%2 == 0 ):
        return 1+ collatz(n/2)
    else:
        return 1+ (collatz((3*n)+1))

def collatz_max(n): 
    if(n==1):
        return n
    if (n%2 == 0 ):
        return max(n, collatz_max(n/2))
    else:
        return max(n, (collatz_max((3*n)+1)))

def nextDirection(direction):
    if (direction[0]==1 and direction[1] == 0):
        return (0,-1)
    if (direction[0]==0 and direction[1] == -1):
        return (-1,0)
    if (direction[0]==-1 and direction[1] == 0):
        return (0,1)
    if (direction[0]==0 and direction[1] == 1):
        return (1, 0)
    
def ullmanSpiral(n):
    matrix = [[0 for x in range(n)] for x in range(n)] 

    if (n%2 == 0):
        indexX = n/2 -1
        indexY = n/2
    else:
        indexX = n/2
        indexY = n/2
    

    currDirectionStreak = 0
    currDirectionStreakLimit = 1
    

    counterForStreakLimitIncrese= 0
    increaseStreakLimit = 2 
    currentNumber = 1
    currentDirection = (1,0)

    while (n*n >= currentNumber):
        matrix[indexY][indexX] = currentNumber
        currentNumber += 1
        indexX = indexX + currentDirection[0]
        indexY = indexY + currentDirection[1]
        currDirectionStreak+=1
        if(currDirectionStreak == currDirectionStreakLimit):
            currDirectionStreak = 0
            currentDirection = nextDirection(currentDirection)
            counterForStreakLimitIncrese +=1
            if(increaseStreakLimit == counterForStreakLimitIncrese):
                currDirectionStreakLimit +=1
                counterForStreakLimitIncrese = 0
    return matrix


def collatzStepCount(upperLimit):
    outputStepCount = open("output/collatzStepCount.txt", "w")
    for i in range (1,upperLimit):
        outputStepCount.write(str(i) + "\t" + str(collatz(i)) + "\n")

def collatzMax(upperLimit):
    outputMax = open("output/collatzMax.txt", "w")
    for i in range (1,upperLimit):
        outputMax.write(str(i) + "\t" + str(collatz_max(i)) + "\n")

def nsdSubstract(a,b, computeStepCount = False):
    print((a,b))
    if (b==a):
        if (computeStepCount):
            return 1
        return a
    if (a>b):
        if (computeStepCount):
            return 1+ nsdSubstract(a-b, b, computeStepCount)
        return nsdSubstract(a-b, b, computeStepCount)
    if (a<b):
        if (computeStepCount):
            return 1+ nsdSubstract(b, a, computeStepCount)
        return nsdSubstract(b, a, computeStepCount)

    
def nsdMod(a, b, computeStepCount = False):
    if (b==0):
        if (computeStepCount):
            return 1
        return a
    if (computeStepCount):
        return 1 + nsdMod(b, a % b, computeStepCount)
    return nsdMod(b, a % b, computeStepCount)

def visualizeNsds():
    size = 400
    bitmapForSubstract = IV122Graphics.BitMap("output/substract.bmp", size, size)
    bitmapForModulo = IV122Graphics.BitMap("output/modulo.bmp", size, size)
    for i in range(1,size):
        for j in range(1,size):
            stepCountSubstract =  nsdSubstract(i,j, True) 
            stepCountMod =  nsdMod(i,j, True) 
            print((i,j, stepCountSubstract, stepCountMod))
            #colorSubstract = (255- stepCountSubstract%255,255-  (stepCountSubstract/255)%255,255-  ((stepCountSubstract/255)/255)%255)
            #colorMod = (255- stepCountMod%255,255-  (stepCountMod/255)%255,255-  ((stepCountMod/255)/255)%255)
            colorSubstract = (255-stepCountSubstract, 0,0)
            colorMod = (255-stepCountMod, 0,0)
            bitmapForSubstract.putPixel(i, size-j, colorSubstract)
            bitmapForModulo.putPixel(i, size-j, colorMod)
    bitmapForSubstract.close()
    bitmapForModulo.close()
    
if __name__ == "__main__":
    
    print("started from console!!!! (hello world)") 
    upperLimit = 8000
    collatzStepCount(upperLimit)
    collatzMax(upperLimit)

    print("-----")

    weirdGrid()
    squaredRainbow()
    Commons.printArray(ullmanSpiral(5))

    print("-----")
    print(nsdMod(54,28))
    print("--")
    print(nsdSubstract(54,28))
    print("-------")
    print(nsdMod(54,30))
    print("--")
    print(nsdSubstract(54,30))
    print("-------")
    print(nsdMod(399,398, True))
    print("--")
    print(nsdSubstract(399,398, True))


    #visualizeNsds()
