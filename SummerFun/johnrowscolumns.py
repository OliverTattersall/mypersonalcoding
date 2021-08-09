import random
lst=[["bob", "greg"],["albert", "john", "ann", "fred"],["sandra", "greg", "bill"]]
def grid_count(grid, target):
    answer1=[0 for i in range(len(grid))]
    longest=0
    for i in range(len(grid)):
        if len(grid[i])>longest:
            longest=len(grid[i])
    answer2=[0 for i in range(longest)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].find(target)!=-1:
                answer1[i]+=1
                answer2[j]+=1


    final_answer=[answer1,answer2]
    return final_answer

print(grid_count(lst, "g"))