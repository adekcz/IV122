import sys, os, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
print("neco")

print("inside If")
parent = "/".join(cmd_folder.split("/")[0:-1])
print("1: " + parent)
parent += "/commonScripts"
print("2: " + parent)
sys.path.insert(0,parent)

import IV122Graphics
import Commons

def squaredRainbow():
    ff = 255
    bitmap = IV122Graphics.BitMap("neco3.jpg", ff, ff)
    for i in range(ff):
        for j in range(ff):
            bitmap.putPixel(i, j, (i,j,ff))
    bitmap.close()

def weirdGrid():
    dim = 400
    stepSize = 20
    svg = IV122Graphics.SVG("neco.svg" ,dim, dim)
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
        print("{0} {1} {2} {3}".format(currDirectionStreak, currDirectionStreakLimit, counterForStreakLimitIncrese, increaseStreakLimit))
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
        Commons.printArray(matrix)
        print("")
    return matrix


if __name__ == "__main__":
    
#    outputStepCount = open("collatzStepCount.txt", "w")
#    outputMax = open("collatzMax.txt", "w")
#    print("started from console!!!! (hello world)") 
#    upperLimit = 8000
#    for i in range (1,upperLimit):
#        print(str(i) + " " + str(collatz(i)))
#        outputStepCount.write(str(i) + "\t" + str(collatz(i)) + "\n")
#
#    print("-----")
#    for i in range (1,upperLimit):
#        print(str(i) + " " + str(collatz_max(i)))
#        outputMax.write(str(i) + "\t" + str(collatz_max(i)) + "\n")
#
#    weirdGrid()
#    squaredRainbow()

    squaredRainbow()
    Commons.printArray(ullmanSpiral(5))
