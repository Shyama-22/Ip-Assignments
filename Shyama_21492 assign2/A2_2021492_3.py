from string import printable


def dec2bin():
    ch = int(input("ENTER CHOICE \n 1. FROM DECIMAL TO BINARY \n 2. FROM BINARY TO DECIMAL\n"))
    if ch == 1:
        lst = []
        n = int(input("ENTER NUMBER: "))
        while n > 0:
            lst.append(n % 2)    
            n = n // 2
        print("NUMER IN BINARY IS: ")
        for i in range(len(lst) - 1, -1, -1): 
            print(lst[i], end="")
    elif ch == 2:
        n = int(input("ENTER NUMBER IN BINARY"))

        decimal = 0
        i = 0
        while (n > 0):
            dec = n % 10  
            decimal = decimal + dec * pow(2, i)
            n = n // 10
            i += 1
        print("NUMBER IN DECIMAL IS: ", end="")
        print(decimal)
    print()


def dec2hex():
    ch = int(input("ENTER CHOICE \n 1. FROM DECIMAL TO HEXADECIMAL \n 2. FROM HEXADECIMAL TO DECIMAL \n"))
    if ch == 1:
        n = int(input("ENTER NUMBER IN DECIMAL FORM: "))
        conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                            5: '5', 6: '6', 7: '7',
                            8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                            13: 'D', 14: 'E', 15: 'F'}
        hex = ''     
        while (n > 0):
            remainder = n % 16
            hex = conversion_table[remainder] + hex
            n = n // 16
        print("NUMBER IN HEXADECIMAL FORM IS: ", end="")
        print(hex)
    if ch == 2:
        conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                            'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

        hex = input("Enter the hexadecimal number: ").strip().upper()
        decimal = 0

        power = len(hex) - 1
 
        for digit in hex:
            decimal += (16 ** power)*conversion_table[digit]
            
            power -= 1

        print("NUMBER IN DECIMAL FORM IS: ")
        print(decimal)
    print()


def dec2oct():
    ch = int(input("ENTER CHOICE \n 1. FROM DECIMAL TO OCTAL \n 2. FROM OCTAL TO DECIMAL \n"))
    if ch == 1:
        lst = []
        n = int(input("ENTER NUMBER: "))
        while n > 0:
            lst.append(n % 8)
            n = n // 8
        print("NUMER IN OCTAL FORM IS: ")
        for i in range(len(lst) - 1, -1, -1):
            print(lst[i], end="")
    elif ch == 2:
        n = int(input("ENTER NUMBER IN OCTAL FORM: "))

        decimal = 0
        i = 0
        while (n > 0):
            dec = n % 10
            decimal = decimal + dec * pow(8, i)
            n = n // 10
            i += 1
        print("NUMBER IN DECIMAL IS: ", end="")
        print(decimal)
    print()


def bin2hex():
    ch = int(input("ENTER CHOICE \n 1. FROM BINARY TO HEXADECIMAL \n 2. FROM HEXADECIMAL TO BINARY \n"))
    if ch == 1:
        n = int(input("ENTER NUMBER IN BINARY"))

        decimal = 0
        i = 0
        while (n > 0):
            dec = n % 10
            decimal = decimal + dec * pow(2, i)
            n = n // 10
            i += 1
        conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                            5: '5', 6: '6', 7: '7',
                            8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                            13: 'D', 14: 'E', 15: 'F'}
        hex = ''
        while (decimal > 0):
            remainder = decimal % 16
            hex = conversion_table[remainder] + hex
            decimal = decimal // 16
        print("NUMBER IN HEXADECIMAL FORM IS: ", end="")
        print(hex)
    elif ch == 2:
        conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                            'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

        hex = input("Enter the hexadecimal number: ").strip().upper()
        decimal = 0

        power = len(hex) - 1

        for digit in hex:
            decimal += (16 ** power)*conversion_table[digit]
            
            power -= 1
            
        decimal = int(decimal)
        lst = []
        while decimal > 0:
            lst.append(decimal % 2)
            decimal = decimal // 2
        print("NUMER IN BINARY IS: ")
        for i in range(len(lst) - 1, -1, -1):
            print(lst[i], end="")
    print()


def bin2oct():
    ch = int(input("ENTER CHOICE \n 1. FROM BINARY TO OCTAL \n 2. FROM OCTAL TO BINARY \n"))
    if ch == 1:
        n = int(input("ENTER NUMBER IN BINARY"))

        decimal = 0
        i = 0
        while (n > 0):
            dec = n % 10
            decimal = decimal + dec * pow(2, i)
            n = n // 10
            i += 1
        lst = []
        decimal = int(decimal)
        while decimal > 0:
            lst.append(decimal % 8)
            decimal = decimal // 8
        print("NUMER IN OCTAL FORM IS: ")
        for i in range(len(lst) - 1, -1, -1):
            print(lst[i], end="")
    elif ch == 2:
        n = int(input("ENTER NUMBER IN OCTAL FORM: "))

        decimal = 0
        i = 0
        while (n > 0):
            dec = n % 10
            decimal = decimal + dec * pow(8, i)
            n = n // 10
            i += 1
        decimal = int(decimal)
        lst = []
        while decimal > 0:
            lst.append(decimal % 2)
            decimal = decimal // 2
        print("NUMER IN BINARY IS: ")
        for i in range(len(lst) - 1, -1, -1):
            print(lst[i], end="")
    print()


def hex2oct():
    ch = int(input("ENTER CHOICE \n 1. FROM HEXADECIMAL TO OCTAL \n 2. FROM OCTAL TO HEXADECIMAL \n"))
    if ch == 1:
        conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                            'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

        hex = input("Enter the hexadecimal number: ").strip().upper()
        decimal = 0
        power = len(hex) - 1
        for digit in hex:
            decimal += (16 ** power)*conversion_table[digit]
            
            power -= 1
        decimal = int(decimal)
        lst = []
        while decimal > 0:
            lst.append(decimal % 8)
            decimal = decimal // 8
        print("NUMER IN OCTAL FORM IS: ")
        for i in range(len(lst) - 1, -1, -1):
            print(lst[i], end="")
    elif ch == 2:
        n = int(input("ENTER NUMBER IN OCTAL FORM: "))

        decimal = 0
        i = 0
        while (n > 0):
            dec = n % 10
            decimal = decimal + dec * pow(8, i)
            n = n // 10
            i += 1
        conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                            5: '5', 6: '6', 7: '7',
                            8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                            13: 'D', 14: 'E', 15: 'F'}
        hex = ''
        while (decimal > 0):
            remainder = decimal % 16
            hex = conversion_table[remainder] + hex
            decimal = decimal // 16
        print("NUMBER IN HEXADECIMAL FORM IS: ", end="")
        print(hex)
    print()


while True:

    print("_MENU_")
    print("Choose the correct option")
    print("1.Convert decimal to binary and vice-versa")
    print("2.Convert decimal to hexadecimal and vice-versa")
    print("3.Convert decimal to octal and vice-versa")
    print("4.Convert binary to hexadecimal and vice-versa.")
    print("5.Convert binary to octal and vice-versa.")
    print("6.Convert hexadecimal to octal and vice-versa")
    print("7.Convert Number With Radix A to Radix B")
    print("8. EXIT")
    choice = int(input())
    if choice == 1:
        dec2bin()
    elif choice == 2:
        dec2hex()
    elif choice == 3:
        dec2oct()
    elif choice == 4:
        bin2hex()
    elif choice == 5:
        bin2oct()
    elif choice == 6:
        hex2oct()
    elif choice == 7:
        import string 
        n=(input("number ="))
        r1=int(input("A = "))
        r2=int(input("B = "))
        def frm(i, r2):
            st = '' 
            while i > 0: 
                st = string.printable[i % r2] + st 
                i //= r2 
            return st.upper()
        def convert(n, r1, r2): 
            return frm(int(n, r1), r2)
        print(convert(n,r1,r2))
        print()
    elif choice == 8:
        print("ENDING PROGRAM")
        break