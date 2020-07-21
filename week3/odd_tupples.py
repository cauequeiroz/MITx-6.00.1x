def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    save = True
    newTup = ()

    for item in aTup:
        if save:
            newTup += (item,)
            save = False
        else: 
            save = True
    
    return newTup

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
# => ('I', 'a', 'tuple')