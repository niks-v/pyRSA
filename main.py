from EncryptionManager import *

enc = EncryptionManager("pub", "priv")

f = open("encryption", "w+")


f.write(enc.EncryptString("hey bb"))

f.close()