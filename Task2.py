string = str(input())
def transformStr():
    a = len(string)
    b = string[0]
    if a > 5:
      print(string[0:5] + '...') 
      if b == 'U' or b == 'u':
        print(string.upper())
      elif b == 'L' or b == 'l':
        print(string.lower())
    else:
        print(string)
transformStr()
