def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 1:
        return aStr == char
    else:
        middle_pos = int(len(aStr)/2)

        if aStr[middle_pos] == char:
            return True
        elif aStr[middle_pos] > char:
            return isIn(char, aStr[:middle_pos])
        elif aStr[middle_pos] < char:
            return isIn(char, aStr[middle_pos:])


print(isIn('a', 'abcdef')) # => True
print(isIn('b', 'abcdef')) # => True
print(isIn('c', 'abcdef')) # => True
print(isIn('d', 'abcdef')) # => True
print(isIn('e', 'abcdef')) # => True
print(isIn('f', 'abcdef')) # => True
print(isIn('g', 'abcdef')) # => False