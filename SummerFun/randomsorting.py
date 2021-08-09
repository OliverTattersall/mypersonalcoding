import random
max=100000
lst=[random.randint(1,max) for i in range(20)]
endlst=[]


# def findlow(lst):
#     if len(lst)>0:
#         low=max+1
#         for i in range(len(lst)):
#             if lst[i]<low:
#                 low=lst[i]
#         endlst.append(low)
#         lst.remove(low)
#         findlow(lst)

# findlow(lst)
# print(endlst)



        

lst2=[1,2,3,4]
def swap(arr, index1, index2):
    temp1=arr[index1]
    temp2=arr[index2]
    arr[index1]=temp2
    arr[index2]=temp1
    return arr


print(swap(lst2, 3,2))
