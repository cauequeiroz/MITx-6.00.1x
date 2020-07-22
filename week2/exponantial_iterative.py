def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1

    for n in range(exp):
        result *= base

    return result

print(iterPower(2, 2))
# => 4