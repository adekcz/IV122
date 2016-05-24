import random
from fractions import gcd
from decimal import *
import sys, os, inspect
#hack to allow importing from specific directory
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parent = "/".join(cmd_folder.split("/")[0:-1])
parent += "/commonScripts"
sys.path.insert(0,parent)

import IV122Graphics
import Commons

globalResult = []
def perm(lst):
    if (len(lst) == 1):
        return [lst]
    result = []
    for i in range(len(lst)):
        # return lst[i] + perm(lst.delete(i))
        listCopy = lst[:]
        popped = listCopy.pop(i)
        for per in perm(listCopy):
            per.append(popped)
            result.append(per)
    return result

def var(lst, k, rep =0):
    if (k == 0):
        return [[]]
    result = []
    for i in range(len(lst)):
        # return lst[i] + var(lst.delete(i),k-1)
        listCopy = lst[:]
        if (rep == 0) :
            popped = listCopy.pop(i)
        else:
            popped = listCopy[i]
        for vari in var(listCopy,k-1, rep):
            vari.append(popped)
            result.append(vari)
    return result

def comb(lst, k, rep =0):
    if (k == 0):
        return [[]]
    result = []
    for i in range(len(lst)):
        if (rep == 0):
            popped = lst.pop(0)
        lstCopy = lst[:]
        if (rep == 1) :
            popped = lst.pop(0)
        for combi in comb(lstCopy,k-1, rep):
            combi.append(popped)
            result.append(combi)
    return result

def computePascalTriangle(rows):
    matrix = [[0 for x in range(rows)] for x in range(rows)] 
    for i in range(rows):
        matrix[i][0] = 1
        matrix[0][i] = 1
    for row in range(1,rows):
        for col in range(1,rows):
            matrix[row][col] = matrix[row][col-1] + matrix[row-1][col]
    return matrix

def drawPascalTriangle(rows, filename, remaindersUpTo= 2):
    colors = ["Black", "Red", "Blue", "Green", "Yellow", "White", "Silver", "Purple", "Magenta"]
    #random.shuffle(colors)

    data = computePascalTriangle(rows)
    for row in range(rows):
        for col in range(rows):
            data[row][col] = data[row][col] % remaindersUpTo

    sizeSquare = 10
    sizeImg = rows * sizeSquare

    
    svg = IV122Graphics.SVG(filename + ".svg", sizeImg, sizeImg)

    for row in range(rows):
        for col in range(rows):
            if(row%2 == 1):
                x = sizeImg/2 - (row/2)*sizeSquare + sizeSquare*col
            else:
                x = sizeImg/2 -sizeSquare/2 - (row/2)*sizeSquare + sizeSquare*col
            svg.setFill(colors[data[row][col]])
            svg.rect(col*sizeSquare, row*sizeSquare, sizeSquare, sizeSquare)

    svg.close()
    return
    
def nthRootByPythonLibrary(a,b):
    return a**b

def getFloatAsFraction(x):
    currX = x
    order = 1
    while(not x.is_integer()):
        x=x*10
        order = order * 10
    return (Decimal(int(x)), Decimal(order))

def nthIntegerPowerNaive(x, exp):
    result = 1
    for i in range(exp):
        result = result * x
    return result

def nthIntegerPowerLogarithmic(x, exp):
    if(exp==0):
        return 1
    result = x
    exponent = 1
    while(exponent*2<= exp):
        result = result*result
        exponent = exponent*2
    #print result, x, exp
    if (exponent != exp):
        #print "powerLogresult beforeMerge: ", result, x, exp
        result = result * nthIntegerPowerLogarithmic(x, exp-exponent)
    #print "powerLogresult: ", result, x, exp
    return result

def heuristicHigh(base, root):
    high = 1
    while pow(high, root) < base:
        high *= 2
    return high

def nthRootBinary(base, root, epsilon, powerFun=nthIntegerPowerLogarithmic):
    high = heuristicHigh(base, root)

    low = 1.0
    value = 0
    while(abs(low - high) > epsilon):
        middle = (high + low) /2.0
        #print "nthrootBinary: ", low, high, middle, value, root
        value = powerFun(middle, root)
        if(value<base):
            low = middle
        if(value>base):
            high = middle
    return low



#get exponent as fraction, simplify,  naive nthpower, find nth-root by binary search
def nthPower(a, b, epsilon = 0.001, powerFun=nthIntegerPowerLogarithmic, rootFun=nthRootBinary):
    fraction = getFloatAsFraction(b)
    gcDivisor = gcd(fraction[0], fraction[1])
    fraction = (fraction[0]/gcDivisor, fraction[1]/gcDivisor)
    #fraction = (Decimal(fraction[0]),Decimal(fraction[1]))
    print fraction
    print "comptuing power",
    power = powerFun(a, fraction[0])
    print power
    print "comptuing root"
    root = rootFun(power, fraction[1], epsilon, powerFun)
    print root



def computePiGregoryLeibnitz(epsilon):
    print "Gregory Leib, epsilon: ", epsilon
    lastVal = 0
    curVal = 4
    sign = 1
    denum = 3
    while(abs(lastVal-curVal) > epsilon):
        lastVal = curVal
        sign = sign * -1
        dif = (sign)*(4.0/denum)
        curVal = curVal + dif
        denum = denum +2
    print "result: ", curVal
    return curVal

def computePiArchimedes(epsilon):
    print "Archimedes, epsilon: ", epsilon
    a = 2.0* 3**(0.5)
    b = 3.0
    lastAvg = 0
    curAvg = 3
    while(abs(lastAvg - curAvg)> epsilon):
        lastA = a
        lastB = b
        a = (2*lastA*lastB)/ (lastA + lastB)
        b = (a*lastB)**0.5
        lastAvg = curAvg
        curAvg = (a+b)/2.0

    print "result: ", curAvg
    return  curAvg

def isInsideCirlce(x, y, r=1):
    return x*x + y*y < r*r
def computePiMonteCarlo(n):
    print "monte carlo, n: ", n

    countIn = 0
    countOut = 0
    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if (isInsideCirlce(x,y)):
            countIn = countIn +1
        else:
            countOut = countOut +1


    result = (4*float(countIn))/n
    print "result: ", result
    return  result

if __name__ == "__main__":
    print nthIntegerPowerLogarithmic(64.75, 500)
    
#    for i in range(2, 9):
#        drawPascalTriangle(500,  "output/trinagle" + str(i), i)
#    print(perm([1,2,3,4]))
#    print("var with rep" + str(var([1,2,3,4],3, True)))
#    print("var without rep" + str(var([1,2,3,4],3, False)))
#    print("comb witrep" + str(comb([1,2,3,4],3, True)))
#    print("comb without rep" + str(comb([1,2,3,4],3, False)))
#
    timer = Commons.Timer()
    timer.start()
    #result = nthPower(10,2.254, 0.001, nthIntegerPowerNaive, nthRootBinary)
    #time = timer.stop()
    #print "power naive, root binary, duration: ", timer.stop(), "computetd val: ", result
    #timer.start()
    #result = nthPower(10,2.254, 0.001, nthIntegerPowerLogarithmic, nthRootBinary)
    #time = timer.stop()
    #print "power logarithmic, root binary, duration: ", timer.stop(), "computetd val: ", result

    computePiGregoryLeibnitz(0.1)
    
    computePiArchimedes(0.1)
    
    computePiArchimedes(0.01)
    
    computePiArchimedes(0.000001)
    
    
    computePiMonteCarlo(100)
    computePiMonteCarlo(1000)
    computePiMonteCarlo(10000000)
