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
