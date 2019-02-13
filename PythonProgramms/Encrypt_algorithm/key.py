import os 
import pyAesCrypt
def decrypt(file):
    print("----------------------------------------------------------------------")
    password = "123"
    BUFFER_SIZE = 512 * 1024

    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, BUFFER_SIZE)

    print("[decrypted '"+str(os.path.splitext(file)[0])+ "'")

    os.remove(file)

def WALK_DECRYPT(dir):
    for name in os.listdir(dir):

        path = os.path.join(dir, name)

        if os.path.isfile(path):
            try:
                decrypt(path)
            except:
                print("Can't decrypt file! /// Exception")
                pass
        else:
                WALK_DECRYPT(path)
                
WALK_DECRYPT("Rubish")
print("----------------------------------------------------------------------")