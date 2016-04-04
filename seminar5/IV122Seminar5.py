import sys, os, inspect
import random
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parent = "/".join(cmd_folder.split("/")[0:-1])
parent += "/commonScripts"
sys.path.insert(0,parent)

import IV122Graphics
import Commons



def angle(p1, p2):

def closure(n):
    size = 400
    img = IV122Graphics.BitMap("closure.jpg", size, size)
    points = generatePoint(20, size)

    for i in range(points):
        for j in range(i, len(points)):





    img.close()
    

def generatePoint(n,upperLimit,  normal = False):
    result = []
    for i in range(n):
        if (normal):
            result.append((random.normalvariate(upperLimit/2,upperLimit/(6*2)), random.normalvariate(upperLimit/2,upperLimit/(6*2)) ))
        else:
            result.append((random.uniform(0, upperLimit), random.uniform(0, upperLimit)))
    
    return result

if __name__ == "__main__":
    n = 20
    print(generatePoint(30, 300))
    print(generatePoint(30, 300, True))

