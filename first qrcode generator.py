try:
    import qrcode
except ImportError:
    print("The qrcode library is not installed.")
    print("Install it using: pip install qrcode")
    exit()

# Function to generate QR code
def generate_qr_code(url, file_name):
    # Create QR code instance
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)

    # Generate QR code
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color="black", back_color="white")

    try:
        img.save(file_name)
        print(f"QR code saved as '{file_name}'")
    except Exception as e:
        print(f"Error saving QR code: {e}")


def main():
    # Enter the URL
    url = input("Enter the URL to generate QR code: ").strip()
    if not url:
        print("Please Enter a Valid URL")
        return

    # Enter file name
    file_name = input("Enter the file name to save the QR code: ").strip()
    if not file_name:
        print("Please don't leave blank space")
        return

    if not file_name.endswith(".png"):
        file_name += ".png"

    generate_qr_code(url, file_name)


if __name__ == "__main__":
    main()
