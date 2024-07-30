#Este arquivo define a classe principal que representa um autômato, e seus principais métodos.

from collections import defaultdict, deque

class AutomatoFinito:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais, deterministico=True):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.deterministico = deterministico
        self.verifica_alfabeto()
        self.deterministico = self.e_deterministico()


    
    def __str__(self):
        return (f"Estado inicial: {self.estado_inicial}\n"
                f"Lista de estados: {self.estados}\n"
                f"Alfabeto: {self.alfabeto}\n"
                f"Transições: {self.transicoes}\n"
                f"Estados finais: {self.estados_finais}\n"
                f"É determinístico? : {self.deterministico}")

    def verifica_alfabeto(self):
        if not all(letra in self.alfabeto for transition in self.transicoes.values() for letra in transition.keys()):
            raise ValueError("A transição apresenta símbolos que não estão presentes no alfabeto.")

    def adiciona_transicao(self, estado_origem, letra, estado_final):
        if letra not in self.alfabeto:
            raise ValueError("A letra não está presente no alfabeto.")
        if estado_origem not in self.estados or estado_final not in self.estados:
            raise ValueError("O Estado de origem não está presente na lista de estados do autômato.")
        
        if self.deterministico:
            if letra in self.transicoes.get(estado_origem, {}):
                raise ValueError("Transição já foi definida para esta letra.")
        
        if estado_origem not in self.transicoes:
            self.transicoes[estado_origem] = {}
        
        self.transicoes[estado_origem][letra] = estado_final

    def processa_string(self, string):
        if self.deterministico:
            return self.processa_string_afd(string)
        else:
            return self.processa_string_afn(string)

    def processa_string_afd(self, string):
        estado_atual = self.estado_inicial
        for letra in string:
            if letra not in self.alfabeto:
                raise ValueError(f"Letra '{letra}' não está presente no alfabeto.")
            if letra not in self.transicoes.get(estado_atual, {}):
                return False
            estado_atual = self.transicoes[estado_atual][letra]
        return estado_atual in self.estados_finais

    def processa_string_afn(self, string):
        estados_atuais = {self.estado_inicial}
        for letra in string:
            if letra not in self.alfabeto:
                raise ValueError(f"Letra '{letra}' noão está presente no alfabeto.")
            
            next_states = set()
            for estado in estados_atuais:
                if letra in self.transicoes.get(estado, {}):
                    next_states.update(self.transicoes[estado][letra])
            
            if not next_states:
                return False
            
            estados_atuais = next_states
        
        return any(estado in self.estados_finais for estado in estados_atuais)

    def e_deterministico(self):
        for estado in self.estados:
            transicoes_estado = self.transicoes.get(estado, {})
            
            for letra in self.alfabeto:
                if letra in transicoes_estado:
                    destino = transicoes_estado[letra]
                    if not isinstance(destino, str) or len(destino) != 1:
                        return False
                else:
                    continue                    
        return True
    

    def afn_para_afd(self):
        if self.deterministico:
            raise ValueError("O automato já é um AFD. ")

        afd_estados = set()
        afd_transicoes = {}
        afd_estado_inicial = frozenset([self.estado_inicial])
        afd_estados_finais = set()
        
        fila = deque([afd_estado_inicial])
        afd_transicoes[afd_estado_inicial] = {}
        
        while fila:
            conjunto_atual = fila.popleft()
            afd_estados.add(conjunto_atual)
            
            for letra in self.alfabeto:
                prox_conjunto = set()
                for estado in conjunto_atual:
                    if letra in self.transicoes.get(estado, {}):
                        prox_conjunto.update(self.transicoes[estado][letra])
                prox_conjunto = frozenset(prox_conjunto)
                
                if prox_conjunto:
                    if prox_conjunto not in afd_transicoes:
                        afd_transicoes[prox_conjunto] = {}
                        fila.append(prox_conjunto)
                    afd_transicoes[conjunto_atual][letra] = prox_conjunto
                    
                    if any(estado in self.estados_finais for estado in prox_conjunto):
                        afd_estados_finais.add(prox_conjunto)
        
        return AutomatoFinito(
            estados=afd_estados,
            alfabeto=self.alfabeto,
            transicoes=afd_transicoes,
            estado_inicial=afd_estado_inicial,
            estados_finais=afd_estados_finais,
            deterministico=True
        )



    def minimiza_afd(self):
        if not self.deterministico:
            raise ValueError("A minimização só é aplicável a AFDs.")

        estados = self.estados
        estado_inicial = self.estado_inicial
        estados_finais = self.estados_finais
        alfabeto = self.alfabeto
        transicoes = self.transicoes

        particoes = {frozenset(estados_finais), frozenset(estados - estados_finais)}

        def obter_transicao_estado(estado):
            return {letra: transicoes.get(estado, {}).get(letra, None) for letra in alfabeto}
        
        def obter_classe_de_equivalencia(estado):
            transicoes_estado = obter_transicao_estado(estado)
            return frozenset(transicoes_estado.items())

        mudanca = True
        while mudanca:
            nova_particao = defaultdict(set)
            for p in particoes:
                for estado in p:
                    classe = obter_classe_de_equivalencia(estado)
                    nova_particao[classe].add(estado)
            
            nova_particoes = set(map(frozenset, nova_particao.values()))
            mudanca = nova_particoes != particoes
            particoes = nova_particoes

        estado_mapeamento = {}
        estado_novo = 0
        for p in particoes:
            for estado in p:
                estado_mapeamento[estado] = f"q{estado_novo}"
            estado_novo += 1
        
        novos_estados = set(estado_mapeamento.values())
        novos_estados_finais = {estado_mapeamento[e] for e in estados_finais if e in estado_mapeamento}
        novos_transicoes = {}
        
        for p in particoes:
            representative = next(iter(p))
            novos_transicoes[estado_mapeamento[representative]] = {}
            for letra in alfabeto:
                destino = transicoes.get(representative, {}).get(letra)
                if destino in estado_mapeamento:
                    novos_transicoes[estado_mapeamento[representative]][letra] = estado_mapeamento[destino]
        
        return AutomatoFinito(
            estados=novos_estados,
            alfabeto=alfabeto,
            transicoes=novos_transicoes,
            estado_inicial=estado_mapeamento.get(estado_inicial, None),
            estados_finais=novos_estados_finais,
            deterministico=True
        )
