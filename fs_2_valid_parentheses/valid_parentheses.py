def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    count_1=0
    count_2=0
    lst= list(parens)
    for p in lst:
        count_1 = lst.count("(") 
        count_2 = lst.count(")")
    return count_1 ==count_2 and parens[0] != ")" and parens[-1] != "()"