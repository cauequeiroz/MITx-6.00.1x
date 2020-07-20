import math

def polysum(n, s):
    '''
    n: number of sides
    s: each sides length

    returns area + square of the perimeter of the regular polygon (rounded to 4 decimal places)
    '''
    perimeter = s * n
    area = (0.25 * n * math.pow(s, 2)) / math.tan(math.pi / n)

    return round(area + math.pow(perimeter, 2), 4)

print(polysum(64, 61)) # => 16453099.1205