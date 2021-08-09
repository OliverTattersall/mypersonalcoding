newstr=''
print("Hello there, welcome to the coder")
print("Chose to decode or encode")
string=input()
print("type what you want to change")
string2=input()
string2=string2.lower()
print("how many digits do you want to shift")
shift=int(input())
list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
if string=="encode":
    for i in range(len(string2)):
        value=string2[i]
        if value==" ":
            newstr=newstr+" "
        else:
            for j in range(len(list1)):
                if list1[j]==value:
                    if j>24-shift :
                        newstr=newstr+string2[i].replace(string2[i],list1[j+shift-26])
                    else:
                        newstr=newstr+string2[i].replace(string2[i],list1[j+shift])
    
    
    
    print("encoded")
    print(newstr)
else:
    for i in range(len(string2)):
        value=string2[i]
        if value==" ":
            newstr=newstr+" "
        else:
            for j in range(len(list1)):
                if list1[j]==value:
                    if j<1:
                        newstr=newstr+string2[i].replace(string2[i],list1[j-shift+26])
                    else:
                        newstr=newstr+string2[i].replace(string2[i],list1[j-shift])
    
    
    
    print("decoded")
    print(newstr)
