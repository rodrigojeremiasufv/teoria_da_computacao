#Este arquivo define as principais funções de criação de um autômato

from Automato import AutomatoFinito

def input_estados():
    estados = input("Insira os estados (separados por vírgula): ").strip().split(',')
    return set(estado.strip() for estado in estados)

def input_alfabeto():
    alfabeto = input("Insira o alfabeto (separados por vírgula): ").strip().split(',')
    return set(letra.strip() for letra in alfabeto)

def input_transicoes(estados, alfabeto):
    transicoes = {}
    for estado in estados:
        transicoes[estado] = {}
        for letra in alfabeto:
            prox_estado = input(f"({estado}) - {letra} -> ").strip()
            if prox_estado == '':
                continue
            elif prox_estado not in estados:
                print(f"Erro: estado '{prox_estado}' não é um estado válido.")
                return None
            else: 
                transicoes[estado][letra] = prox_estado
        if not transicoes[estado]:
            del transicoes[estado]
    if not transicoes:
        del transicoes
    return transicoes

def input_estados_finais(estados):
    estados_finais = input("Insira os estados finais (separados por vírgula): ").strip().split(',')
    conjunto_estados_finais = set(estado.strip() for estado in estados_finais)
    if not conjunto_estados_finais.issubset(estados):
        print("Erro: Alguns estados finais não são válidos.")
        return None
    return conjunto_estados_finais

def input_afd():
    print("Define o AFD: ")
    estado_inicial = input("Insira o estado inicial. ").strip()
    
    estados = input_estados()
    if estado_inicial not in estados:
        print(f"Erro: Estado inicial '{estado_inicial}' não faz parte do conjunto de estados.")
        return None

    alfabeto = input_alfabeto()

    transicoes = input_transicoes(estados, alfabeto)
    if transicoes is None:
        return None

    estados_finais = input_estados_finais(estados)
    if estados_finais is None:
        return None

    deterministic = True 

    return AutomatoFinito(estados, alfabeto, transicoes, estado_inicial, estados_finais, deterministic)