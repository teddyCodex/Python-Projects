import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def start_cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != 'encode' and direction != 'decode':
        print('Invalid Input! Try Again')
        start_cipher()
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

    def caesar_cipher(start_text, shift_amount, cipher_direction):
        end_text = ''
        for i in start_text:
            if i in alphabet:
                if cipher_direction == 'encode':
                    if alphabet.index(i) + shift_amount >= 26:
                        end_text += alphabet[(alphabet.index(i) + shift_amount) % 26]
                    else:
                        end_text += alphabet[alphabet.index(i) + shift_amount]
                elif cipher_direction == "decode":
                    if alphabet.index(i) + shift_amount >= 26:
                        end_text += alphabet[(alphabet.index(i) - shift_amount) % 26]
                    else:
                        end_text += alphabet[alphabet.index(i) - shift_amount]


            else:
                end_text += i
        print(f"The {cipher_direction}d text is {end_text}")
        reset_cipher()

    caesar_cipher(cipher_direction=direction, shift_amount=shift, start_text=text)

def reset_cipher():
    while True:
        reset = input("Type 'yes' to go again. Otherwise, type 'no'.\n").lower()
        if reset == 'yes':
            start_cipher()
            break
        elif reset == 'no':
            exit()
        else:
            print('Invalid Input')

start_cipher()