def poo(a,c):
    d=(a/c+a/2+1)/(2/a+2/c+1)
    print(d)
a=36
counter=0
counter2=0
for c in range(33):
    if (3*c)<=63:
        if a!=0 and c!=0:
            if (a/c+a/2+1)/(2/a+2/c+1) >17 and (a/c+a/2+1)/(2/a+2/c+1)<19:
                #poo(36,c+3)
                print(c)
                counter=counter+1
                
                
                
print(counter)
    
    
