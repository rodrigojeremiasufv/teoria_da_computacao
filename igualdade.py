from Automato import *
import sys
import Automato
from arquivo import *

def compara():
    if len(sys.argv) != 3:
        print("Uso correto: python3 main.py <arquivo_automato.txt> <arquivo_automato2.txt>")
        sys.exit(1)

    nome_arquivo_automato = sys.argv[1]
    nome_arquivo_automato_2 = sys.argv[2]

    try:
        automato = cria_automato_de_arquivo(nome_arquivo_automato)
        print("AUTOMATO 1: -----------------")
        print(automato)
        automato2 = cria_automato_de_arquivo(nome_arquivo_automato_2)
        print("AUTOMATO 2:------------------")
        print(automato2)
        print("-----------------------------")
        min1 = automato.minimiza_afd
        min2 = automato2.minimiza_afd
        print(sao_equivalentes(min1, min2))

    except Exception as e:
        print(f"Erro ao processar os arquivos: {e}")
        sys.exit(1)


def sao_equivalentes(automato1, automato2):
    if not automato1.deterministico:
        automato1 = automato1.afn_para_afd()
    if not automato2.deterministico:
        automato2 = automato2.afn_para_afd()
    
        return (automato1.estados == automato2.estados and
            automato1.transicoes == automato2.transicoes and
            automato1.estado_inicial == automato2.estado_inicial and
            automato1.estados_finais == automato2.estados_finais)
compara()