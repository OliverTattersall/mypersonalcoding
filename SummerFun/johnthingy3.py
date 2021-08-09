import random

lst=[random.randint(1,100) for i in range(random.randint(15,25))]
print(lst)

def split(arr, partition):
    submit=[]
    if len(arr)<=partition:
        submit=arr
        return submit

    else:
        extra=len(arr)%partition
        if extra !=0:

            submit.append(arr[len(arr)-extra:len(arr)+1])
            del arr[len(arr)-extra:len(arr)+1]
        
        temp=[]
        
        for i in range(int(len(arr)/partition)):
            temp.append(arr[0:partition])
            del arr[0:partition]
        for i in range(len(temp)):
            submit.insert(0, temp[len(temp)-i-1])
        return submit



print(split(lst, 5))
