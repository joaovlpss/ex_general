def response(hey_bob):
    hey_bob = hey_bob.strip()  
    
    if not hey_bob or hey_bob.isspace():
        return 'Fine. Be that way!'
    
    if hey_bob.endswith('?') and hey_bob[:-1].isupper() and any(c.isalpha() for c in hey_bob):
        return "Calm down, I know what I'm doing!"
    
    if hey_bob.endswith('?'):
        return 'Sure.'
    
    if hey_bob.isupper() and any(c.isalpha() for c in hey_bob):
        return 'Whoa, chill out!'
    
    return 'Whatever.'

    
    