def is_isogram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    sentence = sentence.lower()
    
    for l in sentence:
        if (l in alphabet):
            alphabet.discard(l)
        elif(l in ['-', ' ', '_']):
            continue
        else:
            return False

    return True