import math
import os


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
