from zipfile import ZipFile
from os import mkdir

line = "--------------------------------------------------------------------------"

def generator(string):

    for word in  string:
        password = word.replace('\n', '')
        archive.setpassword(password.encode())

        try:
            archive.extractall(directory)
        except:
            yield "[False]: " + password
        else:
            yield line + "\n[True]: " + password; return

directory = "ExtractArchive"
try: 
    mkdir(directory)
except FileExistsError: 
    pass

print(line)

with open(input("Dictionary: "), errors='ignore') as dictionary:
    with ZipFile(input("Archive: ")) as archive:
        print(line)
        for password in generator(dictionary):
            print(password)

print(line)