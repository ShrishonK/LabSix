#SHRISHON KUMARASRI ENCODE

def menu():
    print('''
Menu
-------------
1. Encode
2. Decode
3. Quit

Please enter an option: ''', end='')

def encode(value):
    newList = []

    for j in value:
        j = int(j)
        j += 3
        if j == 10:
            j = 0
        if j == 11:
            j = 1
        if j == 12:
            j = 2
        newList.append(j)
    return newList

def decode(value):
    pass


while True:
    menu()
    userInput = int(input())
    if userInput == 1:
        text = input("Please enter your password to encode: ")
        text = list(text)
        encoded = encode(text)
        newStr = [str(k) for k in encoded]
        newStr = ''.join(newStr)
        print('Your password has been encoded and stored!')

    elif userInput == 2:
        decoded = decode(encoded)
        print(f'The encoded password is {newStr}, and the original password is {decoded}.')
    elif userInput == 3:
        break
