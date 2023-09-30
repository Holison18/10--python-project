# a python qr code generator
import qrcode

generate_qrcode = qrcode.make("Kobina Akofi-Holison")
generate_qrcode.save("qr1.png")