from PIL import Image
import pyscreenshot



# grab image
img  = pyscreenshot.grab()

# display the captured screenshot
img.show()

# to save the screenshot
img.save("screenshot.png")