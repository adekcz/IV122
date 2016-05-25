import math
import os
import time

def checkIsBetween(p1, p2, checkedP):
    for i in range(2):
        if ((abs(p1[i] - checkedP[i]) + abs(p2[i] - checkedP[i])) != abs(p1[i] - p2[i])): #comparing false, should use epsilon
            return False
    return True


#p1 and p2 determines line1
#p3 and p4 determines line4
def computeLineIntersection(p1, p2, p3, p4):
    denX = ((p1[0]-p2[0])*(p3[1]-p4[1])-(p1[1] -p2[1])*(p3[0]-p4[0]))
    denY = ((p1[0]-p2[0])*(p3[1]-p4[1])-(p1[1] -p2[1])*(p3[0]-p4[0]))
    if(denX== 0 or denY == 0):
        return -2
    ix = ((p1[0]*p2[1] - p1[1]*p2[0])*(p3[0]-p4[0]) - (p1[0] - p2[0])*(p3[0]*p4[1] - p3[1]*p4[0]))/denX
    iy = ((p1[0]*p2[1] - p1[1]*p2[0])*(p3[1]-p4[1]) - (p1[1] - p2[1])*(p3[0]*p4[1] - p3[1]*p4[0]))/denY
    result = (ix, iy)
    if (not checkIsBetween(p1, p2, result)):
        return -1
    if (not checkIsBetween(p3, p4, result)):
        return -1
    return result


def get_time():
    return int(round(time.time() * 1000))

class Timer():
    def __init__(self):
        self.startTime = 0
        self.endTime = 0
        
    def start(self):
        self.startTime = get_time()

    def stop(self):
        self.endTime = get_time()
        return self.getDif()

    def getDif(self):
        return self.endTime - self.startTime

def equalsDelta(val, delta):
    return  abs(val) <= delta

def createDirs(path_to_output):
    if not os.path.exists(os.path.dirname(path_to_output)):
        try:
            os.makedirs(os.path.dirname(path_to_output))
        except:
            print("problem with creating file, maybe, filename: " + path_to_output)

def max(a,b):
    if (a>b):
        return a
    else:
        return b #don't care about >=

def radToDeg(rad):
    return rad * (180/math.pi)

def degToRad(deg):
    return deg * (math.pi/180)

def printArray(array):
    for line in array:
        print(line)

def cos(deg):
    return math.cos(degToRad(deg))


def sin(deg):
    return math.sin(degToRad(deg))
