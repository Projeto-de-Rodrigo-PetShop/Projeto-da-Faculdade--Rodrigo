from .atendimento import func_atendimento
from .consulta import func_consulta
from .verificador import func_verificador
class veterinario:
    def __init__(self, valor, nome, servico, pagamento):
        self.valor = valor
        self.nome = nome
        self.servico = servico
        self.pagamento = pagamento
           
    def  atendimento(self):
        return func_atendimento(self)
    
    def consulta(self, escolha):
       return func_consulta(self, escolha) 
    
    def verificador(self, escolha):
        return func_verificador(self, escolha)