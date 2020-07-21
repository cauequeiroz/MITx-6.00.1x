def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    result = 0
    
    for item in aDict.values():
        result += len(item)
    
    return result

animals = {
    'a': ['aardvark'],
    'b': ['baboon'],
    'c': ['coati'],
    'd': ['donkey', 'dog', 'dingo']
}

print(how_many(animals))
# => 6