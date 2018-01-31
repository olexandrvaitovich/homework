import math


def correct_size(n, R, chocks, precision=2):
    """
    (int, float, list(tuple), int) -> tuple(tuple(float,float,float))
    Takes positional argument precision
    Determne what chockolates can fit into a box
    """
    correct_chocolate = []
    for chock in chocks:
        sized = False
        if round((chock[0] - 1.17 * 2 * math.pi * R), precision) >= 0:
            if round(R - (math.sqrt(chock[1] / math.pi)), precision) >= 0 and\
                    round(R - (math.sqrt(chock[2] / math.pi)), precision) >= 0:
                sized = True
        if sized:
            correct_chocolate.append(chock)
    return tuple(correct_chocolate)


def input_data():
    """
    ()-> None
    """
    # input data
    n = int(input("n = "))
    R = float(input(" R = "))
    chockolates = []
    for i in range(n):
        chockolates.append((float(input("L=")), float(
            input("s1=")), float(input("s2="))))
    precision = int(input("precision="))
    print(correct_size(n, R, chockolates, precision=precision))


if __name__ == "__main__":
    input_data()
