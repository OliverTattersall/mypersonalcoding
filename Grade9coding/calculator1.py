alphalist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numerolist=['0','1','2','3','4','5','6','7','8','9']
operatorlist=["+",'-','/','*','=','^']
algebra=0
c=0

string=input("solve your math: ")+ ' '
intlist=[]
operlist=[]
datalist=[]
for a in range(len(string)):
    for b in range(len(alphalist)):
        if string[a]==alphalist[b]:
            algebra=algebra+1
            break
if algebra<1:
    while c < len(string):
        for d in range(len(numerolist)):
            if string[c]==str(numerolist[d]):
                if string[c+1]==" ":
                    intlist.append((numerolist[d]))
                    datalist.append(c+2)
                    c=c+1
                elif string[c+2]==" ":
                    intlist.append((numerolist[d]+numerolist[d+1]))
                    datalist.append(c+3)
                    c=c+2
                elif string[c+3]==" ":
                    intlist.append((numerolist[d]+numerolist[d+1]+numerolist[d+2]))
                    datalist.append(c+4)
                    c=c+3
                else:
                    intlist.append((numerolist[d]+numerolist[d+1]+numerolist[d+2]+numerolist[d+3]))
                    datalist.append(c+5)
                    c=c+4
                    
        c=c+1
    print(string)
    for e in range(len(datalist)):
        if len(string)<datalist[e]+1:
            break
        else:
            if string[datalist[e]]=="+":
                print(int(string[:datalist[e]-1])+ int(string[datalist[e]+1:]))
            elif string[datalist[e]]=="-":
                print(int(string[:datalist[e]-1])- int(string[datalist[e]+1:]))
            elif string[datalist[e]]=="/":
                print(int(string[:datalist[e]-1])/ int(string[datalist[e]+1:]))
            elif string[datalist[e]]=="*":
                print(int(string[:datalist[e]-1])* int(string[datalist[e]+1:]))
                

                
                    
                    
    
    
    
    
else:
    print("l")