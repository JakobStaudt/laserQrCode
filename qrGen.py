import pyqrcode

# Text the QR Code will be
qrText = 'Hello World'.upper()
#Error correction level (L, M, Q or H, corresdponds to 7%, 15%, 25%, 30%):
errorLevel = "L"
# width of quiet zone (standard = 4):
quietWidth = 4
# Scale of qrCode and Box
scale = 0.8
# starting Position:
# Empty = lower left (default), c = center, ul = upper left corner, ur = upper right corner, lr = lower right corner
startPos = ""
# Burn dot at machine Zero?
zeroMarker = False
# Burn dots in all corners of quiet Zone?
quietMarkers = False
# Draw Box around quiet Zone?
quietBox = True
# Draw box around code?
codeBox = True
# G-Code to enable Laser
laserEnable = ";Enabling Laser\nM400\nG4 P100\nM106\nM400\n"
# G-Code to disable Laser
laserDisable = ";Disabling Laser\nM400\nM107\nM400\nG4 P250\n"
# G-Code to burn dot
laserDot = laserEnable + "G4 P200\n" + laserDisable

def addSquare(gCode, xStart, yStart, xEnd, yEnd, dir, spacing, retract=True, sideBorders=True):
    xMov = xEnd - xStart
    yMov = yEnd - yStart
    if sideBorders:
        gCode += "\nG0 X" + str(xStart) + " Y" + str(yEnd) + "\n"
        gCode += laserEnable
    gCode += "\nG0 X" + str(xStart) + " Y" + str(yStart) + "\n"
    if not sideBorders:
        gCode += laserEnable
    if dir == 0:
        lineN = int(xMov / spacing)
        for line in range(lineN):
            gCode += "G1 X" + str(xStart + line*spacing) + " Y" + str(yStart) + "\n"
            gCode += "G1 X" + str(xStart + line*spacing) + " Y" + str(yEnd) + "\n"
    else:
        lineN = int(yMov / spacing)
        for line in range(lineN + 1):
            gCode += "G1 X" + str(xStart) + " Y" + str(yStart + line*spacing) + "\n"
            gCode += "G1 X" + str(xEnd) + " Y" + str(yStart + line*spacing) + "\n"
    if sideBorders:
        gCode += "\nG0 X" + str(xEnd) + " Y" + str(yStart) + "\n"
    if retract:
        gCode += "G1 X" + str(xEnd - 0.5 * (yMov/abs(yMov)) * scale) + " Y" + str(yEnd - 0.5 * (yMov/abs(yMov)) * scale) + "\n"
    gCode += laserDisable
    return gCode



qrCode = pyqrcode.create(qrText, error=errorLevel)
qrCode = qrCode.text(quiet_zone=quietWidth)
qrCode = qrCode.strip().split("\n")
qrWidth = len(qrCode)
quietWidth = qrCode.count("0" * qrWidth) / 2


startPos = startPos.lower()

xOffset = 0
yOffset = 0

if startPos == "c" or startPos == "center":
    xOffset = qrWidth*scale / -2
    yOffset = qrWidth*scale / -2
if startPos == "ul" or startPos == "upperleft":
    yOffset = -qrWidth*scale
if startPos == "ur" or startPos == "upperright":
    xOffset = -qrWidth*scale
    yOffset = -qrWidth*scale
if startPos == "lr" or startPos == "lowerright":
    xOffset = -qrWidth*scale

gCode = "G90\nG0 F3000\nG1 F1200\n"

gCode += "G0 X" + str(xOffset) + " Y" + str(yOffset) + " Z0\n"
if quietBox or quietMarkers:
    if quietBox:
        gCode += laserEnable
    if quietMarkers:
        gCode += laserDot
    gCode += "G1 X" + str(xOffset) + " Y" + str(qrWidth*scale + yOffset) + "\n"
    if quietMarkers:
        gCode += laserDot
    gCode += "G1 X" + str(qrWidth*scale + xOffset) + " Y" + str(qrWidth*scale + yOffset) + "\n"
    if quietMarkers:
        gCode += laserDot
    gCode += "G1 X" + str(qrWidth*scale + xOffset) + " Y" + str(yOffset) + "\n"
    if quietMarkers:
        gCode += laserDot
    gCode += "G0 X" + str(xOffset) + " Y" + str(yOffset) + "\n"
    if quietBox:
        gCode += laserDisable
    if codeBox:
        gCode += "G0 X" + str(quietWidth * scale + xOffset) + " Y" + str(quietWidth * scale + yOffset) + "\n"
        gCode += laserEnable
        gCode += "G1 X" + str(quietWidth * scale + xOffset) + " Y" + str((qrWidth-quietWidth)*scale + yOffset) + "\n"
        gCode += "G1 X" + str((qrWidth-quietWidth) * scale + xOffset) + " Y" + str((qrWidth-quietWidth)*scale + yOffset) + "\n"
        gCode += "G1 X" + str((qrWidth-quietWidth) * scale + xOffset) + " Y" + str(quietWidth*scale + yOffset) + "\n"
        gCode += "G1 X" + str(quietWidth * scale + xOffset) + " Y" + str(quietWidth * scale + yOffset) + "\n"
        gCode += laserDisable

elif zeroMarker:
    gCode += laserDot


for lineN in range(len(qrCode[::-1])):
    line = qrCode[lineN]
    inLine = False
    for point in range(len(line)):
        #print(point, lineN)
        if line[point] == "1" and not inLine:
            inLine = True
            lineStart = point
        if line[point] == "0" and inLine:
            inLine = False
            gCode = addSquare(gCode, lineStart*scale + xOffset, lineN*scale + yOffset, point*scale + xOffset, (lineN+1)*scale + yOffset, 1, 0.1)

gCode += "G0 X0 Y0"

#print(gCode)

f = open("t.nc", "w")
f.write(gCode)
f.close()
