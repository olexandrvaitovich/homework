import math


def data_io():
    """console data input and result output"""
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    e = float(input('epsilon = '))
    # check what two sides are equal
    if a == b:
        ans = find_side(a, b, c, e)
    elif b == c:
        ans = find_side(c, b, a, e)
    elif a == c:
        ans = find_side(c, a, b, e)
    else:
        print('wrong input')
    print(ans)


def find_side(a, b, c, e):
    """
    find length of the side of square inscribed in the triangle
    """
    # fing the height of triangle
    h = math.sqrt(a**2 - (c / 2)**2)
    left = 0
    right = c
    x = (left + right) / 2
    # using binary search find the answer
    while abs(c * h / 2 - x * (c - x) / 2 - (h - x) * x / 2 - x * x) > e:
        if c * h / 2 - x * (c - x) / 2 - (h - x) * x / 2 - x * x > 0:
            left = x
        else:
            right = x
        x = (left + right) / 2
    return int(x / e) * e


if __name__ == '__main__':
    data_io()
