def is_armstrong_number(number):
    s = []
    for i in str(number):
        s.append(int(i) ** len(str(number)))
        
    if (sum(s) == number):
        return True
    else:
        return False