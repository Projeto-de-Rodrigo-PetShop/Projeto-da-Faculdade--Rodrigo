from .atendimento import func_atendimento
from .consulta import func_consulta

class veterinario:
    def __init__(self, valor, nome, servico):
        self.valor = valor
        self.nome = nome
        self.servico = servico
           
    def  atendimento(self):
        return func_atendimento(self)
    
    def consulta(self, escolha):
       return func_consulta(self, escolha) 