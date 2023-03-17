

def multadd(lst):
    n = len(lst)

    count = [0 for _ in range(n+1)]

    for val in lst:
        count[val]+=1

    
    sortedList = [0 for _ in range(n)]

    pos = 0

    for i in range(n+1):
        while count[i]>0:
            count[i]-=1
            sortedList[pos]=i
            pos+=1
    print(sortedList, n)
    mult = True
    while(n>1):
        print(sortedList)
        for i in range(0, n, 2):
            # print(i, sortedList[i])
            if mult:
                sortedList[i//2] = sortedList[i]*sortedList[i+1]
                
            else:
                sortedList[i//2] = sortedList[i]+sortedList[i+1]
                
        mult =  not mult
        n= n//2

    print(sortedList)


multadd([7,7,5,5,3,3,1,1])
multadd([1,4,3,6,5,3,2,8])
