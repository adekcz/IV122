import sys, os, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parent = "/".join(cmd_folder.split("/")[0:-1])
parent += "/commonScripts"
sys.path.insert(0,parent)

import IV122Graphics
import Commons

def drawAxes(size, svg):
    svg.line(size/2, 0, size/2, size)
    svg.line(0, size/2, size, size/2)

def plotData(inFile):
    inputData = open(inFile)
    lines = inputData.readlines()

    size = 200

    svg = IV122Graphics.SVG("output/linreg.svg" ,size, size)
    drawAxes(size, svg)
    for line in lines:
        point = line.split(" ")
        svg.circle(1, float(point[0]) +size/2, float(point[1]) + size/2)


    svg.close()


if __name__ == "__main__":
    plotData("linreg.txt")
