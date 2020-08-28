import rsa

def GenerateKeys(size):
    (pubkey, privkey) = rsa.newkeys(size, poolsize=8)
    return [str(pubkey), str(privkey)]

def CreateKeyFiles(size, pubfile, privfile):
    keys = GenerateKeys(size)

    pub = open(pubfile+".txt","w+")
    priv = open(privfile+".txt","w+")

    pub.write(keys[0][10:-1])
    priv.write(keys[1][11:-1])

    pub.close()
    priv.close()

if __name__ == "__main__":
    CreateKeyFiles(4096, "pub", "priv")