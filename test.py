import requests

URL = "https://api.datamuse.com/words"

query = input("Enter the word: ")

parameter = { "rel_rhy" : query}

r = requests.get(URL, parameter)

print(r)
for i in r.json():
    print(i['word'])
