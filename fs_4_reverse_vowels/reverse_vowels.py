def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowel_indexs = []
    vowels =[]
    dict={}
    for [i, letter] in enumerate(s):
        
        if letter.lower() in "aeiou":
            vowel_indexs.append(i)
            vowels.append(letter)
    vowel_indexs.sort(reverse=True)
    for [i,index] in enumerate(vowel_indexs):
        for vowel in vowels[i:i+1]:
            dict[index]=vowel
   
    string =""
    for [i,l] in enumerate(s):
        
        if i in dict.keys():
            
            string += dict[i]
        
       
        else:
            string +=l 
    return string              

    
                
