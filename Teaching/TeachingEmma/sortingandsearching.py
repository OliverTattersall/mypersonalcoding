
def min_val_bin(sequence, item):
    index = 0
    for i in range(len(sequence)):
        if sequence[i]==item:
            index = i
            break

    count = 0
    low = 0
    high = len(sequence) - 1
    while low<=high:
        middle = (low+high)/2
        if middle < index:
            low = middle
        elif middle > index:
            high = middle
        else:
            break

        count+=1

    return count

# [1,2,4,6,7,1,7,3,5,7]
# lst[i] = 1
# [1,2,4,5,1,7, blah]


def insert_sort(lst):

    for i in range(1, len(lst)):
        for j in range(i-1, -1, -1):
            if lst[j+1]<lst[j]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
            else:
                break
            

    return lst

print(insert_sort([i for i in range(20, 0, -1)]))
print(insert_sort([1,5,7,2,4,7,30,12,43,42]))


def steps_back(students):
    for i in range(len(students)):
        for j in range(len(students)):

            return
