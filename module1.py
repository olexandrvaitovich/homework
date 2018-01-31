import math


def data_io():
    """Сonsole data input and result output"""
    # data input
    while True:
        try:
            print('Type lenght of each side:')
            a = float(input('a = '))
            b = float(input('b = '))
            c = float(input('c = '))
            e = float(input('epsilon = '))
            break
        except ValueError:
            print('Wrong input!')

    # check which two sides are equal
    if a == b:
        ans = find_side(a, b, c, e)
    elif b == c:
        ans = find_side(c, b, a, e)
    elif a == c:
        ans = find_side(c, a, b, e)
    else:
        print('Triangle has no equal sides!')
    print("x = ", ans)


def find_side(a, b, c, e):
    """
    (number, number, number, number) -> number
    find length of the side of square inscribed in the triangle

    >>> find_side(10, 10, 12, 0.01)
    4.80029296875
    >>> find_side(12, 12, 20, 0.01)
    4.98046875
    """
    # fing the height of triangle
    h = math.sqrt(a**2 - (c / 2)**2)
    left, right = 0, c
    x = (left + right) / 2
    total_area = c * h / 2 - x * (c - x) / 2 - (h - x) * x / 2 - x * x
    # using binary search find the answer
    while abs(total_area) > e:
        if total_area > 0:
            left = x
        else:
            right = x
        x = (left + right) / 2
        total_area = c * h / 2 - x * (c - x) / 2 - (h - x) * x / 2 - x * x
    return x


if __name__ == '__main__':
    data_io()
