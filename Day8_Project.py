# Day 8 project from 100 Days of Code: The Complete Python Pro Bootcamp course

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)
more = ""


def ceaser(text, shift, direction):
    message = ""
    if direction == "decode":
        shift = shift * -1
    for i in text:
        if i in alphabet:
            z = alphabet.index(i)
            if z + shift >= len(alphabet) and direction == "encode":
                y = shift + z - len(alphabet)
                y = alphabet[y]
                message += y
            elif z - shift <= 1 and direction == "decode":
                y = len(alphabet) + z + shift
                y = alphabet[y]
                message += y
            else:
                y = alphabet[z + shift]
                message += y
        else:
            message += i
    print(f"Here's the {direction}d result: {message}")


while more != "no":

    direction_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text_input = input("Type your message:\n").lower()
    shift_input = int(input("Type the shift number:\n"))

    if shift_input >= 27:
        shift_input = shift_input % 26

    ceaser(text_input, shift_input, direction_input)

    more = input("Type 'yes' if you want to go again, Otherwise type 'no'.").lower()

    if more == "no":
        print("Goodbye")
