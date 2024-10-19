import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=15,
    box_size=25,
    border=10
)

data = "https://www.youtube.com/watch?v=sRrkgjqTTQQ"
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save("textt.png")



