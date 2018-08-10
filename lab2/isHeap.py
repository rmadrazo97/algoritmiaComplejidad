def isHeap(str,i,n):
    e = (n-2)//2
    if( i > e ):
        return True

    try:
        imas1 = str[2*i+1]
    except IndexError:
        imas1 = False
    try:
        imas2 = str[2*i+2]
    except IndexError:
        imas2 = False
    if str[i] >= imas1 and\
       str[i] >= imas2 and\
       isHeap(str, 2*i+1, n) and\
       isHeap(str, 2*i+2, n):
        return True

    return False

str1 = [16,14,10,8,7,9,3,2,4,1]

print(isHeap(str1,0,10))