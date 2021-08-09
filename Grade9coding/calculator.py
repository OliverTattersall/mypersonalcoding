numerolist=[0,1,2,3,4,5,6,7,8,9]
muldiv=["/","*","^"]
operatorlist=["+",'-',"/","*","^"]
alphalist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
intlist=[]
list1=[0]
list2=[]
algebra=0
string2=[]
int1=0
algebralist=[]
leftside=[]
rightside=[]
#string=input("solve your math: ")
string="123 +4*2/1"

for a in range(len(string)):
    for b in range(len(alphalist)):
        if string[a]==alphalist[b]:
            algebra=algebra+1
            algebralist.append(string[a])
            
for c in range(len(algebralist)):
    for d in range(len(alphalist)):
        if algebralist[c]==alphalist[d]:
            print("can't compute more than one variable")
            algebra=algebra+100
            break    

if algebra<1:
    if string[0]!=' ':
        string= " " + string
    for i in range(len(string)):
        for j in range(len(operatorlist)):
            if string[i]==operatorlist[j]:
                list1.append(i)
    for a in range(len(list1)):
        if a==len(list1)-1:
            string2.append(string[list1[a]+1:])
        else:
            string2.append(string[list1[a]+1:list1[a+1]])
    print(list1)
    print(string2)
    for aa in range(len(list1)):
        if string[list1[aa]]=="*":
            int1=float(string2[aa-1])*float(string2[aa])
            string2.remove(string2[aa-1])
            string2.remove(string2[aa-1])
            string2.insert(aa-1, int1)
            list2.append(list1[aa])
            print(string2)
        elif string[list1[aa]]=="/":
            int1=float(string2[aa-1])/float(string2[aa])
            string2.remove(string2[aa-1])
            string2.remove(string2[aa-1])
            string2.insert(aa-1, int1)
            list2.append(list1[aa])
         
    for c in range(len(list2)):
        list1.remove(list2[0])
    
    for b in range(len(list1)):
        if b==len(list1):
            break
        if string[list1[b]]=="+":
            int1=float(string2[0])+float(string2[1])
            string2.remove(string2[0])
            string2.remove(string2[0])
            string2.insert(0,int1)
        elif string[list1[b]]=="-":
            int1=float(string2[0])-float(string2[1])
            string2.remove(string2[0])
            string2.remove(string2[0])
            string2.insert(0,int1)
        elif string[list1[b]]=="*":
            int1=float(string2[0])*float(string2[1])
            string2.remove(string2[0])
            string2.remove(string2[0])
            string2.insert(0,int1)
        elif string[list1[b]]=="/":
            int1=float(string2[0]) / float(string2[1])
            int1=int(int1)
            string2.remove(string2[0])
            string2.remove(string2[0])
            string2.insert(0,int1)
        elif string[list1[b]]=="^":
            int1=float(string2[0]) ** float(string2[1])
            int1=int(int1)
            string2.remove(string2[0])
            string2.remove(string2[0 ])
            string2.insert(0,int1)


    print(string2[0])
    
    
elif algebra>100:
    print("")
else:
    leftside,rightside=string.split("=")
    if string[0]!=' ':
        string= " " + string
    for i in range(len(leftside)):
        for j in range(len(operatorlist)):
            if string[i]==operatorlist[j]:
                list1.append(i)
    for i in range(len(rightside)):
        for j in range(len(operatorlist)):
            if string[i]==operatorlist[j]:
                list2.append(i)
    
    
    
    for a in range(len(list1)):
        if a==len(list1)-1:
            string2.append(string[list1[a]+1:])
        else:
            string2.append(string[list1[a]+1:list1[a+1]])
    for a in range(len(list2)):
        if a==len(list2)-1:
            string2.append(string[list2[a]+1:])
        else:
            string2.append(string[list2[a]+1:list2[a+1]])
        
            
        
            
            
            
            