import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def convert(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn= input("Did you mean %s insted? Enter Y if yes, N if no.." %get_close_matches(w,data.keys())[0])
        if yn=="Y"or"y":
            return data[get_close_matches(w,data.keys())[0]]            
        elif yn=="N"or"n":
            print("You enter wrong word...")
        else:
            print("Please check the word again..")

    else:
        print("The word is invalid. Please double check it...")


word=input("Enter word: ").lower()
output=(convert(word))
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
