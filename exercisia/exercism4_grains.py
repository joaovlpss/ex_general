def square(number):
    grains = [1]
    for i in range(1,64):
        grains.append(grains[i-1] * 2)
    
    if (number > 0 and number <= 64):
        return grains[number - 1]
    else:
        raise ValueError('Square must be between 1 and 64.')

def total():
    grains = [1]
    for i in range(1,64):
        grains.append(grains[i-1] * 2)

    return sum(grains)