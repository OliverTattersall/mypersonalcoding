# Problem: count how many a's between the z's

# ex. 'akjhfdjhzajasjfasksjfhaszasdjazxcbzkjxcxzjcbzkbz


def problem(letters):

    count = 0
    pos = 0
    change = 1
    foundAUG = False

    while pos<len(letters):
        if letters[pos:pos+3]=='AUG':
            foundAUG = True
            change = 3
        
        if foundAUG:
            count +=1
            if letters[pos:pos+3] in ['UGA', 'UAA', 'UAG']:
                break
        
    return count
        

print(problem("akjhfdjhzajasjfasksjfhaszasdjazxcbzkjxcxzjcbzkbz"))