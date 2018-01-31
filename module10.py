def count_chars(line):
    """
    (str) -> list(int)
    Recursively calculates number of capital and small letters
    in the string line
    """
    # base case
    if len(line) == 0:
        return [0, 0]
    # ruccursion step
    else:
        letter = line[-1]
        counter = count_chars(line[:-1])
        if 65 <= ord(letter) <= 90:
            counter[0] += 1
        elif 97 <= ord(letter) <= 122:
            counter[1] += 1
        return counter
