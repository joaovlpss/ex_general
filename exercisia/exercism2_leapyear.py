year = int(input('Insira o ano inteiro: '))

one = (year % 4 == 0)
two = (year % 100 == 0)
three = (year % 400 == 0)

if (one and two and three):
    print('Bissexto.')
elif (one and two):
    print('Nao bissexto.')
elif (one):
    print('Bissexto.')