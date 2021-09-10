# Check even or odd
even = lambda a: not a%2

sum = 0
a , b = 1 , 2
while a < 4000000:
    if even(a):
        sum += a
    a, b = b, a+b

print(sum)