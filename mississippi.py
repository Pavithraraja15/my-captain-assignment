str1 = input ("enter the string")
d1 = dict()
for c in str1:
    d1[c] = d1.get(c,0) + 1
    print (d1)