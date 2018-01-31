def gcd(n, m):
    """
    Return greatest common divisor of 2 integer positive numbers
    """
    if n * m == 0:
        return n + m
    elif n >= m:
        return gcd(m, n % m)
    else:
        return gcd(n, m % n)
