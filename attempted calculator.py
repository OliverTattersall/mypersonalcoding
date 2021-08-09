def calculatorfunction():
    x=input("Choose a number ")
    y=input("choose another ")
    z=input("choose m, d, s or a ")
    x=int(x)
    y=int(y)
    if z=="m":
        print(x*y)
    elif z=="d":
        print(x/y)
    elif z=="a":
        print(x+y)
    else z=="s":
        print(x-y)
    
calculatorfunction()