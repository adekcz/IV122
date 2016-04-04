import IV122Graphics
import Commons
from random import shuffle

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


def comb1(lst, k, rep =0):
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
    #shuffle(colors)

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
    

if __name__ == "__main__":
    for i in range(2, 9):
        drawPascalTriangle(500,  "trinagle" + str(i), i)
