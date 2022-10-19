print("###################################################")

while True:
    print('\nPLEASE CHOOSE WHAT YOU WANT TO DO')
    print('1. BINARY TO DECIMAL'
          '\n2. DECIMAL TO BINARY'
          '\n3. OCTAL TO DECIMAL'
          '\n4. DECIMAL TO OCTAL'
          '\n5. HEXADECIMAL TO DECIMAL'
          '\n6. DECIMAL TO HEXADECIMAL'
          '\n7. BINARY TO OCTAL'
          '\n8. OCTAL TO BINARY'
          '\n9. BINARY TO HEXADECIMAL')
    choice = int(input("Enter the number of your choice: "))
    print('---------------------------------------------------')

    if choice == 1:
        number = input('ENTER THE NUMBER YOU WANT TO CONVERT:    ')
        DECIMALOFBINARY = int(number, 2)
        print(f'ANSWER: '
              f'\n DECIMAL TO BINARY OF {number} is:  {DECIMALOFBINARY}\n')
        continue;

    elif choice == 2:
        number = int(input('ENTER THE NUMBER YOU WANT TO CONVERT:    '))
        BINARYOFDECIMAL = bin(number)
        print(f'ANSWER: {BINARYOFDECIMAL}')
        continue;

    elif choice == 3:
        number = input('ENTER THE NUMBER YOU WANT TO CONVERT:    ')
        OCTALTODECIMAL = int(number, 8)
        print(f'ANSWER: '
              f'\n OCTAL TO DECIMAL OF {number} is:  {OCTALTODECIMAL}\n')
        continue;

    elif choice == 4:
        number = int(input('ENTER THE NUMBER YOU WANT OT CONVERT:    '))
        DECIMALTOOCTAL = oct(number)
        print(f'ANSWER: '
              f'\n DECIMAL TO OCTAL OF {number} is:  {DECIMALTOOCTAL}\n')
        continue;

    elif choice == 5:
        number = input('ENTER THE NUMBER YOU WANT TO CONVERT:        ')
        HEXADECIMALTODECIMAL = int(number, 16)
        print(f'ANSWER: '
              f'\n HEXADECIMAL TO DECIMAL OF  {number} is:  {HEXADECIMALTODECIMAL}\n')
        continue;

    elif choice == 6:
        number = int(input('ENTER THE NUMBER YOU WANT TO CONVERT:    '))
        DECIMALTOHEXADECIMAL = hex(number)
        print(f'ANSWER: '
              f'\n DECIMAL TO HEXADECIMAL OF  {number} is:  {DECIMALTOHEXADECIMAL}\n')
        continue;

    elif choice == 7:
        number = input('ENTER THE NUMBER YOU WANT TO CONVERT:    ')
        BINARYTOOCTAL = oct(int(number, 2))
        print(f'ANSWER: '
              f'\n BINARY TO OCTAL OF  {number} is:  {BINARYTOOCTAL}\n')
        continue;

    elif choice == 8:
        number = input('ENTER THE NUMBER YOU WANT TO CONVERT:       ')
        OCTALTOBINARY = bin(int(number, 8))
        print(f'ANSWER: '
              f'\n OCTAL TO BINARY OF  {number} is:  {OCTALTOBINARY}\n')
        continue;

    elif choice == 9:
        number = input('ENTER THE NUMBER YOU WANT TO CONVERT:     ')
        BINARYTOHEXADECIMAL = hex(int(number, 2))
        print(f'ANSWER: '
              f'\n BINARY TO HEXADECIMAL OF  {number} is:  {BINARYTOHEXADECIMAL}\n')
        continue;

    else:
        break;

        print('____________________________________________________________')
