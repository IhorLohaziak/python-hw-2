num = input()
def sumNum(num):
    x = [int(a) for a in str(num)]
    c = sum(x)
    r = str(c)
    z = len(r)
    if z == 2:
        print(r[1])
    elif z == 1:
        print(r[0])
sumNum(num)