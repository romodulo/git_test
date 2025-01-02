print("hello")
#func def's
def i_range_Next(iterable: int=3):
    for i in range(0,iterable):
        print("Next: ")
def iterator(myList : list):
    for i in myList:
        if i != '':
            print(f'\'{i}\'')
        else:
            print(f'{i}')
def buildANewList(myListCopy: list):
    buildANewList= []
    for i in myListCopy:
        wordToAdd = ""
        for ii in i:
            if ii != "|":
                wordToAdd += ii
            else:
                ii = "\|" #test:for edu.p:can i use <ii> instead?
                wordToAdd += ii
        buildANewList.append(wordToAdd)
    return buildANewList

#opens and closes file
filename = "../README.md"
with open(filename, "r") as fn:
    read_data = fn.read()

#checks if file has closed:
print(f'has the file closed: {fn.closed}') #outputs either True or False

#print contents of file:
myList = read_data.split('\n')
myListCopy = myList[:]
print(len(myList))

#main script: 
iterator(myListCopy)
i_range_Next(3)
# print(myListCopy)
# i_range_Next(3)

aNewList = buildANewList(myListCopy)
iterator(aNewList)
i_range_Next()

#create a new string for a future file:
aString = ""
for i in aNewList:
    aString += i + '\n'
print(aString)

filename2 = "../BUILT_AREADME.md"

with open(filename2, "w") as fl2:
    fl2.write(aString)

print(fl2.closed)
