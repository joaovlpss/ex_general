def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence_set = set(sentence.lower())

    return alphabet.issubset(sentence_set)