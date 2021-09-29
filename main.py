# Dictionary with basic functionalities using python string methods:

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

# json text:-
# data = '{' \
#        '"smog":"air pollutants",' \
#        '"adhesive":"sticking objects together"' \
#        '}'


# def close_match(word, data):
#     return get_close_matches(word, data.keys())[0]


def finder(word):
    if word.lower() in data:
        return data[word.lower()]
    if word.upper() in data:
        return data[word.upper()]
    if word.title() in data:
        return data[word.title()]

    # for item in matches:
    #     if item in data.keys():
    #         return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s ?" % get_close_matches(word, data.keys())[0])
        decide = input("Press y or n :")
        if decide == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == 'n':
            return "Not found"
        else:
            return "Enter y or n only."
    else:
        return "Not found"


# for key, value in data.items():  # Alternate one
#     if key == word.lower():
#         print(value)

word = input("Enter any word: ")
# matches = close_match(word, data)
output = finder(word)

if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)

# for key in data.items():
#     match = re.search(word, key.data)
#     if match:
#         print(match.group(0))
#     else:
#         exit()

