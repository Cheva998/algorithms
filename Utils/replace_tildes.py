def replace_tildes(s):
    '''
    Take the tildes from vowels in a string and transforms them
    into their "non-vowel" form
    '''
    a,b = 'áéíóúüÁÉÍÓÚÜ','aeiouuAEIOUU'
    trans = str.maketrans(a,b)
    return s.translate(trans)