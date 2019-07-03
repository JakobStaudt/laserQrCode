# laserQrCode
Engraving QR-Codes with CNC Lasers
![QR-Code](https://i.imgur.com/AAAwKHO.jpg)
## What it is:
This Program lets you generate G-Code for engraving QR-Codes with a CNC Laser.
## What you need:
A Python 3 installation and the PyQRCode library.
You can install the PyQRCode-Library with "pip install PyQRCode".
(And a CNC Laser Cutter of course)
## How you use it:
Open the qrGen.py file with your text editor, adjust the parameters, execute it, and a new .nc-file should appear.
That's your G-Code. Run this with your Laser and you should get a nice QR-Code.
## Adjustable Parameters:
### qrText
This is the Data that should be encoded into the Code.
If you use only Caps, numbers, space, $, %, *, +, -, ., /, and :, a smaller Encoding is used which makes the QR-Code smaller.
### errorLevel
This is the Error correction Level used. The Levels possible are L, M, Q or H.
The Levels correspond to the error Tolerances of 7%, 15%, 25% or 30% of data Loss that can be tolerated.
If you choose a higher error tolerance, the Code gets bigger but can be scanned more reliably.
### quietWidth
This specifies how wide the quiet Zone around the Code should be. Normally, this is 4 modules wide.
### scale
This lets you scale the whole program up or down.
### invert
This inverts the dark and bright areas of the QR-Code. Useful if you want to Laser stamps or remove protective coating to etch.
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
If this is enabled, the Laser moves into the black region it lasered before turning off to avoid burning the edge if disabling the laser takes some time.
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
### travelSpeed
The Speed used for travelling while the Laser is disabled in your machine's speed unit.
### cutSpeed
The Speed used for cutting while the Laser is enabled in your machine's speed unit.
