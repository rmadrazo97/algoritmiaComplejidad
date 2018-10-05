from Mergesort import mergesort
from jug import TaskGenerator
import shutil, os

#-------TaskGenerator--------------TaskGenerator-------------TaskGenerator---



@TaskGenerator
def distributedRead(file):
    fileR = open(file)
    #getting all lines in the file. 
    sentences1 = []
    for x in fileR:
        value = x
        #if last char = "\n" do not add it. 
        if (value[len(value)-1] == "\n"):
            value = value[0:len(value)-1]
            #sentences1.append(value)
        sentences1.append(value)
    #print(sentences1)
    return sentences1

        #returning sentences, with one sentence(line) per item in array. 

@TaskGenerator
def distributedWrite(sentences):
    if os.path.exists("orderedFile.txt"):
        os.remove("orderedFile.txt")
    else:
        print("Creating File to write answer.")
    ordered = []
    ordered = mergesort(sentences)
    print(ordered)
    [Writer(item) for item in ordered]

@TaskGenerator
def Writer(item):
    fileW = open("orderedFile.txt", "a")
    print(item,"\n")
    fileW.write(item)
    fileW.write("\n")
    


readed = distributedRead("unorderedFile.txt")
distributedWrite(readed)

#--------------------------------------------
try:
    shutil.rmtree("main.jugdata")
except:
    pass
#--------------------------------------------
