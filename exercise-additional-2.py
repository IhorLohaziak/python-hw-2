str1 = input()
str2 = input()
def commonStr():
    comparison = list(set(str1) & set(str2))
    a = ''.join(comparison)
    b = a.split()
    c = ''.join(b)
    print(c)
commonStr()