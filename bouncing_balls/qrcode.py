import qrcode
from PIL import Image

Logo_Link = "csumb.jpg"
logo = Image.open(Logo_Link)

basewidth = 100

wpercent = basewidth/float(logo.size[0])
hsize = int(logo.size[1]*float(wpercent))

logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

QRcode = qrcode.QRCode(
    error_correction = qrcode.constants.ERROR_CORRECT_H
)

url = "https://www.youtube.com/watch?v=5qap5aO4i9A"

QRcode.add_data(url)

QRimg = QRcode.make_image(fill_color = "blue", back_color = 'white').convert('RGB')

diff = (QRimg.size[0]-logo.size[0])//2, (QRimg.size[1]-logo.size[1])//2
QRimg.paste(logo, diff)

QRimg.save("mynewQRcode.jpg")
img = Image.open("mynewQRcode.jpg")
img.show()