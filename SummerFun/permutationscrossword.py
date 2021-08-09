from itertools import permutations

letters=input()
lst=list(permutations(letters))
lst2=[]
for i in range(len(lst)):
    lst[i]=list(lst[i])
    str=""
    for j in range(len(lst[i])):
        str+=lst[i][j]
    lst[i]=str.lower()
    if  lst[i][3]=="i":
        str2="h"+lst[i][:4]+"-"+lst[i][4:]
        lst2.append(str2)
    

print(lst2)