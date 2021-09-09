def multiples(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    return False

sum = 0
for i in range(1, 1000):
    if multiples(i):
        sum += i

print(sum)