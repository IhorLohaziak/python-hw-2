num = input()
def sumNum(num):
    x = [int(a) for a in str(num)]
    c = sum(x)
    r = str(c)
    z = len(r)
    if z == 2:
        a1 = int(r)
        if a1 < 10:
            print(r[1])
        elif a1 >= 10:
            f = str(a1)
            f1 = int(f[0])
            f2 = int(f[1])
            f3 = f1 + f2
            print(f3)
    elif z == 1:
        print(r[0])
sumNum(num)