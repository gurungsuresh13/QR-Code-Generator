# Make sure you have installed qrcode and Pillow (PIL) libraries using: pip install qrcode[pil]
import qrcode
from PIL import Image

data = "https://www.youtube.com/watch?v=01e5SAvJfpg"

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=5,
)
qr.add_data(data)
qr.make(fit=True)

# Create a QR code image
qr_img = qr.make_image(fill_color="black", back_color="white")

# Save the image
qr_img.save("qr_code.png")

# Open the image using PIL
try:
    img = Image.open("qr_code.png")
    img.show()
except Exception as e:
    print(f"An error occurred: {e}")
