import requests
import json
# num = input()
num = 5

try: 
    r = requests.get("https://random-word-api.herokuapp.com/word?number=20")
    if r.status_code==200:
        x = r.json()
        val=""
        for i in x:
            if len(i)==num:
                val= i
                break
        
        
except:
    print()

def wordle(word):
    for i in range(6):
        test = input("write your word: ")
        for j in range(len(test)):
            print()
        print()