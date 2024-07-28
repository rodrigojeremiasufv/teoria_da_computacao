#Este arquivo define a classe principal que representa um autômato finito.

class AutomatoFinito:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais, deterministico=True):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.deterministico = deterministico
        self.verifica_alfabeto()
    
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

