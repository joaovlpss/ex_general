def equilateral(sides):
    a, b, c = sides
    if(a + b < c or a + c < b or c + b < a or a + b + c == 0):
        return False
    
    if (a == b == c):
        return True
    else:
        return False
    
def isosceles(sides):
    a, b, c = sides

    if(a + b < c or a + c < b or c + b < a or a + b + c == 0):
        return False
    
    if(a == b or b == c or c == a):
        return True
    else:
        return False
    
    
def scalene(sides):
    a, b, c = sides

    if(a + b < c or a + c < b or c + b < a or a + b + c == 0):
        return False
    
    if(a != b and a != c and b != c):
        return True
    else:
        return False