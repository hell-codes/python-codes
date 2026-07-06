def doubleStuff(alist):
    '''Overwrite each element in alist with double its value.'''
    for position in range(len(alist)):
        alist[position] = 2 * alist[position]

thing = [2, 5, 9]
doubleStuff(thing)
print(thing)  
