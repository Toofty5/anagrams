import json
from flask import Flask, request
from collections import defaultdict
from random import choice,shuffle

app = Flask(__name__)

if __name__ == "__main__": 
  print("Hello, anagram!")

# Generate word_dict, keyed to the size of the character set
DICTIONARY = open("./sowpods") 
words = [line.strip() for line in DICTIONARY.readlines()]
word_dict = defaultdict(list)

for word in words:
  word_dict[len(set(word))].append(word)

@app.route("/anagrams")
def anagrams():
  difficulty = request.args.get("difficulty")
  return json.dumps({"result": generate_puzzle(difficulty)})

def generate_puzzle(prompt):
  # call your puzzle generator entrypoint here, and return the result from this
  # function.
  answer = choice(word_dict[int(prompt)])
  puzzle = list(answer)
  shuffle(puzzle)
  return ''.join(puzzle)

# used to generate a character set for the unsolvable puzzle 
def charset(difficulty):
  return_me = []
  for i in range(difficulty):
    return_me.append(chr(ord('a')+i))
  return return_me

def unsolvable_puzzle(length, difficulty):
  chars = charset(difficulty)
  return_me = []
  for i in range(length):
    return_me.append(choice(chars))

  return ''.join(return_me)

