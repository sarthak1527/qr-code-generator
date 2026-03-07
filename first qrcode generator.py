try:
    import qrcode
except ImportError:
    print("The qrcode library is not installed.")
    print("Install it using: pip install qrcode")
    exit()


# Function to generate QR code
def generate_qr_code(data, file_name):
    # Create QR code instance
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)

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
    # Enter the text or URL
    data = input("Enter text or URL to generate QR code: ").strip()
    if not data:
        print("Please enter some text or URL")
        return

    # Enter file name
    file_name = input("Enter the file name to save the QR code: ").strip()
    if not file_name:
        print("Please don't leave blank space")
        return

    # Ensure .png extension
    if not file_name.endswith(".png"):
        file_name += ".png"

    generate_qr_code(data, file_name)


if __name__ == "__main__":
    main()
