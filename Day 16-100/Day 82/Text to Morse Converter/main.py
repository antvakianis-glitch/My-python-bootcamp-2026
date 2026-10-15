MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--',
    'Z': '--..',   '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',
    '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',
    '0': '-----',  ' ': '/',      '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '!': '-.-.--', '-': '-....-', '/': '-..-.',  '@': '.--.-.', '(': '-.--.',
    ')': '-.--.-'
}

def convert_to_morse_code(text):
    return ' '.join(MORSE_CODE_DICT.get(char,char) for char in text.upper())

def main():
    print("--- Text to Morse Code Converter ---")

    while True:
        user_input = input("\nEnter text to convert (or type 'exit' to quit): ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        if not user_input:
            print("Please enter some text to convert.")
            continue

        result = convert_to_morse_code(user_input)
        print(f"\nConverted Morse Code:\n{result}")

if __name__ == '__main__':
    main()