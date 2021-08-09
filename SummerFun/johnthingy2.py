def sum_non_negative(sum):
    tempinput=int(input(""))
    if tempinput<0:
        return sum
    else:
        sum+=tempinput
        return sum_non_negative(sum)

sum_non_negative(0)