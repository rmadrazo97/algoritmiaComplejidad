from jug import TaskGenerator
import shutil, os


#----------------------------------------------------------------------------
#-------TaskGenerator--------------TaskGenerator-------------TaskGenerator---
#----------------------------------------------------------------------------

@TaskGenerator
def Write():
    global sentences1
    if os.path.exists("orderedFile2.txt"):
        os.remove("orderedFile2.txt")
    else:
        print("Creating File to write answer.")
        print("\n")
        print("\n")
    print("Antes de MS:   ", sentences1)
    mergesort(sentences1)
    print("Despues de MS: ", sentences1)
    for item in sentences1:
        [writer(item)]
    #print(ordered)
    #file --> orderedFile2.txt
    #print("despues de MG: ", sentences1)
    #[writer(item) for item in sentences1]
    #shutil.rmtree("pruebas.jugdata")




@TaskGenerator
def mergesort(arr):
    
    #print("Splitting ",arr)
    if len(arr)>1:
        
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        mergesort(left)
        mergesort(right)


        i=0
        j=0
        k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k]=left[i]
                i=i+1
            else:
                arr[k]=right[j]
                j=j+1
            k=k+1
        
        while i < len(left):
            arr[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            arr[k]=right[j]
            j=j+1
            k=k+1 

    #print("\n","Merging ",arr)
    return arr

@TaskGenerator
def distributedRead(file):
    fileR = open(file)
    #getting all lines in the file. 
    global sentences1
    for x in fileR:
        value = x
        #if last char = "\n" do not add it. 
        if (value[len(value)-1] == "\n"):
            value = value[0:len(value)-1]
            #sentences1.append(value)
        sentences1.append(value)
        print("valor: ",value)

    print("leido:         ", sentences1)
    #print(sentences1)
    #return sentences1


@TaskGenerator
def writer(i):
    print("Writing: ", i)
    fileIn = open("orderedFile2.txt", "a")    
    fileIn.write(i)
    fileIn.write("\n")


#-------------------------------------------
#-------------MAIN-Program------------------
#-------------------------------------------

#==========================
#global variables
sentences1 = []
#==========================
distributedRead("unorderedFile.txt")
#mergesort(sentences1)
Write()


try:
    shutil.rmtree("pruebas.jugdata")
except:
    pass
#---------------------------------------------------------------------
#---------------------------------------------------------------------