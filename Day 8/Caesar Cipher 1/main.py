alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text, shift):
        if direction == "encode":
        # TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
                cipher_text = ""
                for letter in text:
                    if letter not in alphabet:
                        cipher_text += letter
                    else:
                        position = alphabet.index(letter)
                        shifted_position = (shift + position) % 26
                        cipher_text += alphabet[shifted_position]
                print(f"The encoded text is {cipher_text}")

        elif direction == "decode":
                cipher_text = ""
                for letter in text:
                    if letter not in alphabet:
                        cipher_text += letter
                    else:
                        position = alphabet.index(letter)
                        shifted_position = (position - shift) % 26
                        cipher_text += alphabet[shifted_position]
                print(f"The encoded text is {cipher_text}")

should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    encrypt(text,shift)
    restart = input(f"Do you want to try again. Press Yes or No?")
    if restart == "no":
        should_continue = False
        print("Goodbye!")



# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

