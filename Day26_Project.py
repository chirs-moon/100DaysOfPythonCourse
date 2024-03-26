# Day 26 project from 100 Days of Code: The Complete Python Pro Bootcamp course

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

signs = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

output_list = [signs[letter] for letter in word]
print(output_list)