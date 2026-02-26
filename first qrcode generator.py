try: 
    import qrcode
except ImportError:    
    print("The qrcode library is not installed. Please install it using 'pip install qrcode' and try again.")
    exit()
#Function to generate QR code
def generate_qr_code(url,file_name):
#Create QR code instance
    qr=qrcode.QRCode(version=1,box_size=10,border=5)
    qr.add_data(url)
    #Generate QR code
    qr.make(fit=True)
    #Create an image from the QR code
    img=qr.make_image(fill_color="black",back_color="white")
   try:
    img.save(file_name)
    print(f"QR code saved as '{file_name}'")
except Exception as e:
    print(f"Error saving QR code: {e}")     
#enter the url and file name to save the QR code
url=input("Enter the URL to generate QR code: ")
if not url.strip():
     print("Please Enter a Valid URL")
     exit()
file_name=input("Enter the file name to save the QR code (with .png extension): ")
if not file_name.strip():
     print("Please don't leave blank space")
     exit()
if not file_name.endswith(".png"):
    file_name+=".png"
generate_qr_code(url,file_name) 
