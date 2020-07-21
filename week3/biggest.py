def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    largest_key = ('', 0)

    for item in aDict:
        item_length = len(aDict[item])
        
        if item_length > largest_key[1]:
            largest_key = (item, item_length)
    
    return largest_key[0]

animals = {
    'a': ['aardvark'],
    'b': ['baboon'],
    'c': ['coati'],
    'd': ['donkey', 'dog', 'dingo']
}

print(biggest(animals))
# => 'd'