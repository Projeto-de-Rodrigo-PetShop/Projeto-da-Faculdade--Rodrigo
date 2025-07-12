
def func_consulta(self,escolha):
           if self.valor < 0:
            print("\nO valor não pode estar negativado")
           
           nome_servico, preco = self.servico[escolha]  
           if self.valor >= preco:
              print(f"O cliente {self.nome} pagou o serviço: {nome_servico}")
           else:
              print(f"\nO cliente {self.nome} deu um valor insuficiente para o serviço {nome_servico}")  
