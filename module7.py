def calculate_sqr(n):
    """
    Calculate squre of a positive integer recursively using
    n^2 = (n-1)^2 + 2(n-1)+ 1 formula
    """
    if n == 1:
        return 1
    else:
        return calculate_sqr(n - 1) + 2 * (n - 1) + 1
