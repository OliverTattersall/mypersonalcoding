length=int(input("How many years the money will be compounding: "))
invested=int(input("Amount of money added each year: "))
sublength=int(input("Number of years money will be added: "))
inter=int(input("Interest at which money will be compounding; "))
tax=int(input("Amount the investment will be taxed: "))



def compound(years, addingyears, sum, interest):
    money=float(sum)
    totalpaid=0
    for i in range(years):
        print("year "+ str(i+1) +": "+str(money))
        if i>(addingyears-1):
            money=money*(1+interest/100)
        else:
            money=money*(1+interest/100)+sum
            totalpaid+=sum

    return money, totalpaid
print(list(compound(length,sublength, invested, inter)))