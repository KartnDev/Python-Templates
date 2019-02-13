def createGenerator() :
    mylist = range(3)
    for i in mylist :
        yield i*i

print(createGenerator())

for i in createGenerator():
    print(i)