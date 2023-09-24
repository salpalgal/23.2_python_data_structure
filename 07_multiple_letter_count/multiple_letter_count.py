def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}

    """
    
    
    dict={}
    
    for char in phrase:
        count=1
        if char in dict:
            dict[char] = count+1
            return dict
            
        dict[char]=count
        
        

    return dict
