def multiples(n):
    """ 
    Determine if the multiple is three or five?

    Args:
        n (int): Input integer

    Returns:
        boolean: If the number is divisible by 3 or 5, it returns True, otherwise it returns False.
    """
    if n % 3 == 0 or n % 5 == 0:
        return True
    return False

sum = 0
for i in range(1, 1000):
    if multiples(i):
        sum += i

print(sum)