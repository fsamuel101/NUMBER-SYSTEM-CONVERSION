import pyttsx3

pyttsx3.speak('Please use this code properly')
pyttsx3.speak('Enter the letter x when you are done')
pyttsx3.speak('wait')
pyttsx3.speak('fuck you stupid son of a bitch')

while True:
    print("\n\nPRESS x IF YOU ARE DONE: ")
    print('--------------------------------------------------------------')
    number = input('Enter the number you want: ')
    print("\n")

    if number == 'x' or 'X': break;

    try:
        print(f"Decimal to Binary form: {bin(int(number))[2:]}")  # decimal to binary
    except:
        print("No Decimal to Binary form")
    try:
        print(f"Binary to Decimal form: {int(number, 2)}")  # binary to decimal
    except:
        print('No Binary to Decimal form')
    try:
        print(f"Hexadecimal to Decimal: {int(number, 16)}")  # hexadecimal to decimal
    except:
        print("No Hexa decimal to Decimal form: ")
    try:
        print(f"Decimal to Hexadecimal: {hex(int(number))[2:]}")  # decimal to hexadecimal
    except:
        print("No Decimal to  Hexadecimal form")
    try:
        print(f"Octal to Decimal form: {int(number, 8)}")  # octal to decimal
    except:
        print("No Octal to Decimal form")
    try:
        print(f"Decimal to Octal form: {oct(int(number))[2:]}")  # decimal to octal
    except:
        print("No Decimal to Octal form")
    try:
        print(f"Binary to Octal: {oct(int(number, 2))[2:]}")  # binary to octal
    except:
        print("No Binary to Octal form")
    try:
        print(f"Octal to Binary form: {bin(int(number, 8))[2:]}")  # Octal to binary
    except:
        print("No octal to binary form")
    try:
        print(f"Binary to Hexadecimal: {hex(int(number, 2))[2:]}")  # Binary to hexadecimal
    except:
        print("No binary to Hexadecimal form")
    try:
        print(f"Hexadecimal to Binary form: {bin(int(number, 16))[2:]}")  # Hexadecimal to binary
    except:
        print("No Hexadecimal to Binary form")
