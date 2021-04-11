def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
# w/o using swapcase method
    # cap = to_swap.lower()
    # low = to_swap.upper()

    
    # result = ''
    # for ltr in phrase:
    #     if ltr == cap:
    #         result+=low
    #     elif ltr == low:
    #         result+=cap
    #     else:
    #         result += ltr 
    # return result
    
# using swapcase method
    result = ''
    for ltr in phrase:
        if to_swap.lower() == ltr or to_swap.upper() == ltr:
            result +=ltr.swapcase()
        else:
             result += ltr
    return result