import math
from PIL import Image, ImageDraw
import cv2

def getMouseCoords(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global gndStationXPix, gndStationYPix
        gndStationXPix = x
        gndStationYPix = y


image = cv2.imread("C:/Users/green/PycharmProjects/pythonProject/dog.jfif")

gndStationImg = Image.open("C:/Users/green/PycharmProjects/pythonProject/dog.jfif")
draw = ImageDraw.Draw(gndStationImg)

heightFt = float(input("What is the height of this image (ft)"))
widthFt = float(input("What is the width of this image (ft)"))

distance = float(input("What distance was the rocket from the ground station"))
theta = float(input("What angle is the rocket from the ground station (Due East is 0 deg)")) * -0.01745329252

rocketXFt = distance * math.cos(theta)
rocketYFt = distance * math.sin(theta)

pixelWidth = image.shape[1]
pixelHeight = image.shape[0]

gridWidth = round(pixelWidth / (widthFt / 250.0))
gridHeight = round(pixelHeight / (heightFt / 250.0))

for i in range(0, pixelWidth, gridWidth):
    draw.line([(i, 0), (i, pixelHeight)])

for i in range(0, pixelHeight, gridHeight):
    draw.line([(0, i), (pixelWidth, i)])

print("Click on where the ground station is and then press the zero key")

cv2.imshow("Image", image)
cv2.setMouseCallback("Image", getMouseCoords)

cv2.waitKey(0)

rocketXPix = round(gndStationXPix + ((rocketXFt / widthFt) * pixelWidth))
rocketYPix = round(gndStationYPix + ((rocketYFt / heightFt) * pixelHeight))


for x in range(gndStationXPix - 2, gndStationXPix + 2):
    for y in range(gndStationYPix - 2, gndStationYPix + 2):
        draw.point((x, y), fill="blue")

for x in range(rocketXPix - 2, rocketXPix + 2):
    for y in range(rocketYPix - 2, rocketYPix + 2):
        draw.point((x, y), fill="red")


gndStationImg.save("GroundStation.png")



print("Blue is Ground Station, Red is Rocket, Top-Left of the image is (0,0)")