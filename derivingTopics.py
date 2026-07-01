import spacy
from collections import deque
nlp = spacy.load("en_core_web_md")

with open("paper1.txt", "r") as f:
    text = f.read()
    
doc = nlp(text)    

#define key-word class
class KeyWord:
    def __init__(self, text, count):
        self.text = text
        self.count = count

    def __repr__(self):
        return f"KeyWord({self.text}, {self.count})"

# Create an array of all proper noun occurrences
textArray= deque()

textArray = []

current_phrase = []

for token in doc:
    if token.pos_ in ["PROPN", "NOUN"]:
        current_phrase.append(token.text)
    else:
        if 1 <= len(current_phrase) <= 3:
            textArray.append(" ".join(current_phrase))
        current_phrase = []

# Handle the last phrase if the document ends with a noun
if 1 <= len(current_phrase) <= 3:
    textArray.append(" ".join(current_phrase))
        
#print (textArray)

# Create KeyWord objects with counts
visited = []
keywords = []
count = 0

for i in range(len(textArray)):
    if textArray[i] in visited:
        continue

    count = 1

    for j in range(i + 1, len(textArray)):
        if textArray[j] == textArray[i]:
            count += 1

    visited.append(textArray[i])
    keywords.append(KeyWord(textArray[i], count))

#print(keywords)

ranked_array = deque()

while len(keywords) > 0:
    first = 0

    for i in range(len(keywords)):
        if keywords[i].count > keywords[first].count:
            first = i

    ranked_array.append(keywords[first])
    keywords.pop(first)

print(ranked_array)

###### so far, code is able to 
