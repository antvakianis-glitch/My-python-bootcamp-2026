import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_nato = {row.letter:row.code for (index, row) in nato_data.iterrows()}

is_on = True
while is_on:
    word = input("Enter a word: ").upper()
    try:
        phonetic_code = [new_nato[letter] for letter in word]
    except KeyError:
        print("please enter a valid word not numbers")
    else:
        print(phonetic_code)
        pandas.DataFrame(phonetic_code).to_csv("phonetic_code_word.csv")
        is_on = False
















































