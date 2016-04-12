from PIL import Image
import Commons 
import math

class Graphics:
    def __init__(self, path_to_output, width, height):
        return

    def close():
        return

class SVG(Graphics):
    def __init__(self, path_to_output, width, height):
        Commons.createDirs(path_to_output)
        self.outputFile = open(path_to_output, "w")
        self.outputFile.write( "<svg version=\"1.1\"\r\n     baseProfile=\"full\"\r\n     width=\"{0}\" height=\"{1}\"\r\n     xmlns=\"http://www.w3.org/2000/svg\">\n".format(width, height))
        self.setStroke()
        self.setFill()

    def close(self):
        self.outputFile.write( "</svg>\n" )
        self.outputFile.close()

    def setStroke(self, c = "Black"):
        self.strokeColor = c

    def setFill(self, c = "Black"):
        self.fillColor  = c

    def rect(self,x1,y1, width, height):
        self.outputFile.write("<rect x=\"{0}\" y=\"{1}\" width=\"{2}\" height=\"{3}\" fill=\"{4}\" />\n".format(x1, y1, width, height, self.fillColor))

    def line(self, x1, y1, x2, y2):
        self.outputFile.write("<line x1=\"{0}\" y1=\"{1}\"  x2=\"{2}\" y2=\"{3}\" stroke=\"{4}\" stroke-width=\"{5}\"/>\n".format(x1, y1, x2, y2, self.strokeColor, 2))

    def circle(self, r, x, y):
        self.outputFile.write("<circle cx=\"{0}\" cy=\"{1}\" r=\"{2}\" stroke=\"{3}\" fill=\"{4}\" stroke-width=\"{5}\"  />\n".format(x,y,r, self.strokeColor, self.fillColor, 2)) 

    def close(self ):
        self.outputFile.write("</svg>\n")

degreesInCircle = 360 
class Turtle():
    def __init__(self, path_to_output, width, height, xStart, yStart):
        self.svg = SVG(path_to_output,width,height)    
        self.x = xStart
        self.y = yStart
        self.pen = True
        self.orientation = 90;

    def forward(self, length):

        newX = length * math.sin(Commons.degToRad(self.orientation))  + self.x
        newY = length * math.cos(Commons.degToRad(self.orientation))  + self.y
        
        if(self.pen):
            self.svg.line(self.x,self.y, newX, newY)

        self.x = newX 
        self.y = newY

    def back(self, size):
        self.left(180)
        self.forward(size)
        self.left(180)

    def left(self, angle):
        self.orientation = (self.orientation + angle) % degreesInCircle

    def right(self, angle): #nebo left(360-angle)
        self.orientation = (self.orientation - angle) % degreesInCircle

    def penUp(self):
        self.pen = False

    def penDown(self):
        self.pen = True

    def close(self):
        self.svg.close()

class BitMap(Graphics):
    def __init__(self, path_to_output, width, height):
        Commons.createDirs(path_to_output)
        self.path = path_to_output
        self.image = Image.new("RGB", (width, height), (255,255,255))
        return

    def close(self):
        self.image.save(self.path, "JPEG")


    def putPixel(self, x, y, color = (255, 255,255)):
        self.image.putpixel((x,y), color)



#existuje nejake str.format()
#koukni na jakysi python notebook

if __name__ == "__main__":
    print(math.sin(math.pi/60))
    print("Graphics module loaded from console")
    bitmap = BitMap("neco.jpg", 400, 300)
    for i in range(100):
        bitmap.putPixel(i, i, (i,i,i))
    bitmap.close()
    

    turtle = Turtle("myFirstTurtle.svg", 400, 400, 200, 200)
    for i in range(3):
        turtle.forward(100)
        turtle.left(90)
    turtle.close()


