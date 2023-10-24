import math
def score(x, y):
    dist = math.sqrt((x)*(x) + (y) * (y))

    if dist <= 1:
        return 10
    elif dist > 1 and dist <= 5:
        return 5
    elif dist > 5 and dist <= 10:
        return 1
    else:
        return 0