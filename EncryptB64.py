from EncryptionManager import *
import base64

mgr = EncryptionManager("pub", "priv")

with open("test.png", "rb") as image_file:
    img = base64.b64encode(image_file.read())

out = open("testpng.txt", "w+")

out.write(mgr.EncryptString(str(img)))

out.close()