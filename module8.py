def calculate_sum(n, m):
    """
    Count sum of type 1^m + 2^m + … + n^m, where n and m are positive integers
    """
    if n == 1:
        return 1
    else:
        return calculate_sum(n - 1, m) + n**m
