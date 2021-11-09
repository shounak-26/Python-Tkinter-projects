import pyqrcode
import qrcode

img = qrcode.make("https://understandingfea.blogspot.com/")
img.save("FEA.jpg")