import random

source=[1,4,6,2,1]
test=[[random.randint(1,20) for j in range(random.randint(10,20))] for i in range(random.randint(2,5))]
print(test)

def intersect(source, others):

    final=[0 for i in range(len(source))]
    final2=[]
    for i in range(len(source)):
        for j in range(len(others)):
            for k in range(len(others[j])):
                if source[i]==others[j][k]:
                    final[i]+=1
                    break

    for i in range(len(final)):
        if final[i]==len(others):
            final2.append(source[i])

    source=final2
    return source

print(intersect(source, test))

