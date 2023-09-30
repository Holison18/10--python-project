# a python qr code generator
import qrcode

# define a function to create qr code when user enters message or url
def qrGenerator(message_url,Version=1,Box_size=40,Border=3,Fit=True,Fill_color="black",Back_color="white",saveas="img.png"):
    # set the features of the qr code
    features = qrcode.QRCode(version = Version, box_size = Box_size, border = Border)

    # add the url or message to create the qr code with
    features.add_data(message_url)

    features.make(fit=Fit)

    generate_image = features.make_image(fill_color = Fill_color ,back_color = Back_color )
    generate_image.save(saveas)

    print("QR code generated check folder for qr!")

print("\n\n\t\t\tGENERATE QR")
message = input("Message/URL: ")
version = int(input("Version: "))
box_size = float(input("Box_size: "))
border = float(input("Border: "))
fit = bool(input("Fit (True/False): "))
fill_color = input("Fill Color: ")
background = input("Background color: ")
saveas = input("Save QR as: ")

# call the qrGenerator function
qrGenerator(message,version,box_size,border,fit,fill_color.lower(),background.lower(),saveas)