# laserQrCode
Engraving QR-Codes with CNC Lasers
## What it is:
This Program lets you generate G-Code for engraving QR-Codes with a CNC Laser
## What you need:
A Python 3 installation and the PyQRCode library
## How you use it:
Open the qrGen.py file with your text editor, adjust the paramters, execute it, and a new t.nc file should appear.
Thats your g-Code. Run this with your Laser and you should get a nice QR-Code.
## Adjustable Parameters:
### qrText
This is the Data that should be encoded into the Code.
If you use only Caps, numbers, space, $, %, *, +, -, ., /, and :, a smaller Encoding is used.
### errorLevel
This is the Error correction Level used. The Levels possible are L, M, Q or H.
The Levels correspond to the error Tolerances of 7%, 15%, 25% or 30% of data Loss that can be tolerated.
If you choose a higher error tolerance, the Code gets bigger but can be scanned more reliably.
### quietWidth
This specifys how wide the quiet Zone around the Code should be. Normally, this is 4 modules wide.
### scale
This lets you scale the whole program up or down.
### spacing
This is the spacing between the Lines the laser uses to raster solid Black
### startPos
The Default starting Position is the lower left of the code.
If you set it to "ul"/"upperLeft", it starts in the upper left corner.
If you set it to "ur"/"upperRight", it starts in the upper right corner.
If you set it to "lr"/"lowerRight", it starts in the lower right corner.
If you set it to "c"/"center", it starts in the Center of the Code.
### sideBorders
If this is enabled, the Laser draws vertical lines at the borders of rastered black regions.
### cornerRetract
If this is enabled, the Laser moves into the black region it lasered before before turning off to avoid burning the edge if disabling the laser takes some time.
### zeroMarker
If this is enabled, the Laser burns a small dot at machine zero at the start of the Program.
Only useful if startPos is not "center", or you will have a dot in your Code.
### quietMarkers
If this is enabled, the Laser burns a dot in each of the Corners of the quietZone
### quietBox
If this is enabled, the Laser draws a Box around the quietZone
### codeBox
If this is enabled, the Laser draws a Box around the QR-Code
### laserEnable
This string contains the G-Code to enable the Lase. use \n for new line.
### laserDisable
This string contains the G-Code to disable the Lase. use \n for new line.
### laserDot
This string contains the G-Code to burn a dot with the Laser.