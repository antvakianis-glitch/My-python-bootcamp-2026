import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_nato = {row.letter:row.code for (index, row) in nato_data.iterrows()}

word = input("Enter a word: ").upper()

phonetic_code = [new_nato[letter] for letter in word]

pandas.DataFrame(phonetic_code).to_csv("phonetic_code_word.csv")












































