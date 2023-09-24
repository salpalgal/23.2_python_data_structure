def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    list=[]
    split_list= phrase.split(" ")
    for word in split_list:
        list.append((word.lower().capitalize()))
    return str(" ".join(list))
 
