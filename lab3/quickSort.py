def quicksort(str):
    #if p<r
        #q= partition(A,p,r)
        #quicksort(A,p,q-1)
        #quicksort(A,q+1,r)
    
    if len(str) == 1 or len(str) == 0:
        #ret arreglo si no contiene más de 1. 
        return str
        
    else:
        pivot = str[0]
        i = 0
        for j in range(len(str)-1):
            #for j = p to r-1
            if str[j+1] < pivot:
                
                #if A[j]<= x
                str[j+1],str[i+1] = str[i+1], str[j+1]
                #exchange A[i] with A[j]
                i += 1
                #i=i+1
        
        str[0],str[i] = str[i],str[0]
        #exchange A[i+1] with A[r]
        str_1 = quicksort(str[:i])
        str_2 = quicksort(str[i+1:])
        #quicksort(A,p,q-1)
        #quicksort(A,q+1,r)
        str_1.append(str[i])
        return str_1 + str_2

A =[5,10,15,32,55,21,40,2,3,76,89,28,9,7]
print(quicksort(A))