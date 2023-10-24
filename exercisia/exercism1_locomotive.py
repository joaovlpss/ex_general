'''
Exercicios do exercism.org
Exercicio de aprendizado - Locomotive Engineer
'''

def get_list_of_wagons(*args):
    return list(args)

def fix_list_of_wagons(wag1, wag2):
    # Assinala os primeiros dois elementos de wag1 a first e second
    # e depois todo o resto a rest com o operador de desempacotamento *.
    first, second, *rest = wag1

    # Cria uma nova lista wag1_fixed, desempacotando rest e somando a first e second
    # para que fiquem no final.
    wag1_fixed = *rest, first, second

    # Cria uma nova lista wag_final, somando wag1_fixed e wag2 desempacotados
    # com o operador *. Retorna wag_final.
    wag_final = *wag1_fixed, *wag2
    return wag_final

def add_missing_stops(route, **kwargs):
    # Sortei os kwargs baseado na ordem indicada pelos numeros de stop,
    # gerando uma lista de tuplas.
    sorted_stops = sorted(kwargs.items(), key=lambda item: item[0])

    # Cria um dicionario com uma unica chave 'stops', e seu valor e uma
    # lista com todos os valores das tuplas na lista sorted_stops.
    stops = {'stops': [stop[1] for stop in sorted_stops]}

    # Retorna um dicionario formado pelos valores de route e stops,
    # desempacotado pelo operador **.
    return {**route, **stops}

def extend_route_information(d1, d2):
    return {**d1, **d2}

def fix_wagon_depot(l1):
    sol = [[],[],[]]

    # Iniciando i como 0, percorre a coluna j que vai de 0 a 2.
    # sol[j] recebe l1[i][j], ou seja, sol[0] recebera l1[0][0], entao
    # sol[1] recebera l1[0][1]...
    # Percorre cada linha da matriz l1 e coloca na coluna em sol.
    for i in range(0,3):
        for j in range(0,3):
            sol[j].append(l1[i][j])
    
    return sol
