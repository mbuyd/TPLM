#toki pona language model
import json
dic =json.load(open("sample.json"))
words = input().split(" ")

def search(word):
    for i in dic:
        if word in dic[i]:
            return dic[i][word]
        
#Python | Word Similarity using spaCy
        
for word in words:
    print(search(word), end = " ")


