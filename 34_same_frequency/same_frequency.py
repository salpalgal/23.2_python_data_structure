def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    list1=[]
    list2=[]
    set1=()
    set2=()
    list_num1 = list(str(num1))
    list_num2 = list(str(num2))
    for num in list_num1:
        counted = list_num1.count(num)
        tup = (num,counted)
        list1.append(tup)
       
    for num in list_num1:
        counted = list_num2.count(num)
        tup = (num,counted)
        list2.append(tup)
    set1 = set(list1)
    set2=set(list2)
    if set1 ^ set2:
        return False
    return True
    
