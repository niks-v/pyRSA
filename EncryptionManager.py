import rsa

class EncryptionManager:
    def __init__(self, pubkeyfile, privkeyfile):
        self.pubkeyfile = self.OpenKeyFile(pubkeyfile)
        self.privkeyfile = self.OpenKeyFile(privkeyfile)

    def OpenKeyFile(self, keyFile):
        keyFile = open(keyFile+".txt", "r").read()
        key = keyFile.split(", ")
        if len(key) == 2:
            key = rsa.PublicKey(int(key[0]), int(key[1]))
            print(key)
            return key
        else:
            key = rsa.PrivateKey(int(key[0]), int(key[1]), int(key[2]), int(key[3]), int(key[4]))
            print(key)
            return key
        
        keyFile.close()
        return key

    def EncryptString(self, toEncrypt):
        toEncrypt = toEncrypt.encode('utf8')
        return str(rsa.encrypt(toEncrypt, self.pubkeyfile))

    def DecryptString(self, toDecrypt):
        return rsa.decrypt(toDecrypt, self.privkeyfile).decode('utf-8')