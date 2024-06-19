from character import *
import os

os.system('clear')
word = input("A word will be: ").lower()
os.system('clear')

wordList = ["_"] * len(word)
print(status0)
print(*wordList)
print()
char = input("Say a word: ").lower()
os.system('clear')

i = 0
while True:

    if char in word:
        for idx, wd in enumerate(word):
            if char == wd:
                wordList[idx] = char
    else:
        i += 1

    if i == 7:
        print("!! You Lose !!".center(20, ' '))
        print(f"The answer is '{word}'".center(20, ' '))
        break

    if '_' not in wordList:
        print("!! You Win !!".center(20, ' '))
        break

    print(screen[i])
    print(*wordList)
    print()
    char = input("Say a word: ").lower()
    os.system('clear')