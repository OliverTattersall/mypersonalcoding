# import random

prompt="Player {0}'s hand: "
score_message="Player 1: {0}, Player 2: {1}"
tie_message="Tie!"
win_message="Player {0} wins!"

def ro_sham_bo(total_winning_throws):
    scores=[0,0]
    options=["paper", "rock", "scissors"]
    i=0
    while i<1:
        end=""
        p1=input(prompt.format(1))
        p2=input(prompt.format(2))
        # p1=options[random.randint(0,2)]
        # p2=options[random.randint(0,2)]
        num1=options.index(p1)
        num2=options.index(p2)
        if num1==num2:
            end=tie_message
        else:
            if num1!=2 and (num1+1)==num2:
                scores[0]+=1
            elif num1==2 and num2==0:
                scores[0]+=1
            elif num1!=0 and (num1-1)==num2:
                scores[1]+=1
            elif num1==0 and (num2==2):
                scores[1]+=1


            end=score_message.format(scores[0], scores[1])
            
        
        # print(prompt.format(1)+p1)
        # print(prompt.format(2)+p2)
        if scores[0]==total_winning_throws or scores[1]==total_winning_throws:
            i=1
        if i!=1:
            print(end)
    if scores[0]>scores[1]:
        print(win_message.format(1))
    elif scores[0]<scores[1]:
        print(win_message.format(2))
    else:
        print(tie_message)
    return None



# ro_sham_bo(random.randint(3,6))