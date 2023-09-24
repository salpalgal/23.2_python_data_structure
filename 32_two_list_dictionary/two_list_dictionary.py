def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    
    # for val in values:
    #     dict ={k:val for k in keys}
    # return dict
    dict={}
    new_dict=[]
    for k in keys:
        
        index = keys.index(k)
            
        for val in values[index:index+1:]:
           
            dict[k]=val
    for end in keys[len(values):]:
        dict[end]= None
    
    return dict
        