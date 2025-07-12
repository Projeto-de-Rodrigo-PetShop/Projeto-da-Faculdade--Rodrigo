
def func_consulta(self,escolha):
           if self.valor < 0:
            print("\nO valor não pode estar negativado")
            
           nome_servico, preco = self.servico[escolha]  
           if self.valor >= preco:
              self.valor -= preco
              print(f"\nO cliente {self.nome} pagou o serviço: {nome_servico}, ainda sobrou {self.valor} reais")
           else:
                print(f"\nO cliente {self.nome} não tem dinheiro suficiente para pagar o serviço: {nome_servico}")
              