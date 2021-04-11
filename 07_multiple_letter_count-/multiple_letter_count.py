def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # new_set = {char for char in phrase}
    # return {char: phrase.count(char) for char in new_set}
    # letter in object order is incorrect -- try again
    counter = {}
    for ltr in phrase:
        counter[ltr]=counter.get(ltr,0)+1
    return counter