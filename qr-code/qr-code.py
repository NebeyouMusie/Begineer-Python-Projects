import pyqrcode
from pyqrcode import QRCode

# string for the QR code
s = "https://www.youtube.com"

# generating the QR code
url = pyqrcode.create(s)

# Create and save the png file
url.svg("youtube.svg", scale = 8)