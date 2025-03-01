import qrcode
from PIL import Image

def generate_qr(text, filename="qrcode.png", fill_color="blue", back_color="white", logo_path=None):
    qr = qrcode.QRCode(
        version=4,  
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,  
        border=4  
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    if logo_path:
        logo = Image.open(logo_path)
        logo = logo.resize((50, 50))  
        pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, pos, logo if logo.mode == "RGBA" else None)

    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    data = input("Enter text or URL: ")
    generate_qr(data, logo_path="logo.png") 