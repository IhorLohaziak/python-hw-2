string = str(input())
def transformStr():
    a = len(string)
    b = string[0]
    if a > 5:
        if b == 'U' or b == 'u':
            print(string[0:5].upper() + '...')
        elif b == 'L' or b == 'l':
            print(string[0:5].lower() + '...')
        else:
            print(string[0:5] + '...')
    elif a < 5:
        if b == 'U' or b == 'u':
            print(string.upper())
        elif b == 'L' or b == 'l':
            print(string.lower())
        else:
            print(string)
transformStr()
