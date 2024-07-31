#Este arquivo define funções importantes para criação de automatos a partir de arquivos

from Automato import AutomatoFinito

#cria um novo automato a partir de um arquivo
def cria_automato_de_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as nome_arquivo:
        linhas = [line.strip() for line in nome_arquivo if line.strip()]

    estados = linhas[0].split(',')
    estados = [estado.strip() for estado in estados]

    alfabeto = linhas[1].split(',')
    alfabeto = [simbolo.strip() for simbolo in alfabeto]

    transicoes = {}
    for linha in linhas[2:-2]:
        estado_origem, letra, estado_destino = linha.split(',')
        estado_origem = estado_origem.strip()
        letra = letra.strip()
        estado_destino = estado_destino.strip()
        if estado_origem not in transicoes:
            transicoes[estado_origem] = {}
        transicoes[estado_origem][letra] = estado_destino

    estado_inicial = linhas[-2].strip()

    estados_finais = linhas[-1].split(',')
    estados_finais = [estado.strip() for estado in estados_finais]

    automato = AutomatoFinito(
        estados=estados,
        alfabeto=alfabeto,
        transicoes=transicoes,
        estado_inicial=estado_inicial,
        estados_finais=estados_finais,
    )
    return automato

def carrega_arquivo_strings(nome_arquivo_strings):
    with open(nome_arquivo_strings, 'r') as nome_arquivo:
        strings = [line.strip() for line in nome_arquivo if line.strip()]
        return strings


#Processa todas as strings presentes em um arquivo, linha por linha 
def processa_strings_arquivo(automato, nome_arquivo_strings):
    strings_para_processar = carrega_arquivo_strings(nome_arquivo_strings)
    resultado = {}
    for string in strings_para_processar:
        resultado[string] = automato.processa_string(string)
    return(resultado)
        

automato = cria_automato_de_arquivo("./automatos/automato.txt")
automato.processa_string("ABA")