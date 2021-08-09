import time
x=2
count=0
while x>1:
    count=count+1
    print(count)
    time.sleep(1)
    y=input(": ")
    if y=="stop":
        count=0
        break