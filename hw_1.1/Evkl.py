a = int(input())
b = int(input())
if b > a:
    a, b = b, a
c = a - (b * (a // b))
a = b
b = c
while c != 0:
    c = a - (b * (a // b))
    a = b
    b = c
print(a)


a = 1071
b = 462
c = 2
while (a % c !=0 and b % c != 0):
    print(c)
    c += 1
print(c)
