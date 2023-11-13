# Ceasar Cipher
# Encoding Words
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#e.g. 
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
restart = 'y'
 
while restart == 'y':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift_pre = int(input("Type the shift number:\n"))
    shift = shift_pre % 26

    def caesar(plain_text, shift_amount, direction):
        cipher_text = ''
        for letter in plain_text:
            position = alphabet.index(letter)
            if direction == 'encode':
                new_position = position + shift_amount
            if direction == 'decode':
                new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The {direction} text by {shift} shift number is:\n {cipher_text}")

    caesar(plain_text=text, shift_amount=shift, direction=direction)
    restart = input("Would you like to restart this program? y or n:\n")
