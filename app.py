import json
from difflib import SequenceMatcher, get_close_matches
from os import error, initgroups

def translate(word):
    word = word.lower()
    if word in data:
        return printList(data[word])
    elif title(word) in data:
        return printList(data[title(word)])
    elif word.upper() in data:
        return printList(data[word.upper()])
    elif len(get_close_matches(word, data.keys(), n=5, cutoff=0.8)) > 0:
        answer = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if answer == "Y":
            return printList(data[get_close_matches(word, data.keys())[0]])
        elif answer == "N":
            return "Okay, please try again"
        else:
            return "We doesn't understand your query"
    else:
        return "The Word doesn't exist..."

def printList(l):
    i = 0
    for a in l:
        i += 1
        print(f'{i}: {a}')


def title(word):
    return word.capitalize()

data = json.load(open("data.json"))

userInput = input("Enter a word: ").lower()
print(translate(userInput))