import math


def correct_size(n, R, chocks, precision=2):
    """
    (int, float, list(tuple), int) -> tuple(tuple(float,float,float))
    Takes positional argument precision
    Check if chocolates fit into the box
    """

    def circle_lenght(R):
        """
        number -> number
        return length of circumference from radius
        """
        return 2 * math.pi * R

    def circle_radius(S):
        """
        number -> number
        find radius of the circle from area
        """
        return math.sqrt(S / math.pi)

    correct_chocolate = []
    for chock in chocks:
        fits = False
        if round((chock[0] - 1.17 * circle_lenght(R)), precision) >= 0:
            if round(R - circle_radius(chock[1]), precision) >= 0 and\
                    round(R - circle_radius(chock[2]), precision) >= 0:
                fits = True
        if fits:
            correct_chocolate.append(chock)
    return tuple(correct_chocolate)


def data_io():
    """
    ()-> None
    """
    try:
        # input data
        n = int(input("n = "))
        R = float(input(" R = "))
        chockolates = []
        for i in range(n):
            chockolates.append((float(input("L=")), float(
                input("s1=")), float(input("s2="))))
        precision = int(input("precision="))
        print(correct_size(n, R, chockolates, precision=precision))
    except ValueError:
        print('Wrong input')


if __name__ == "__main__":
    data_io()
