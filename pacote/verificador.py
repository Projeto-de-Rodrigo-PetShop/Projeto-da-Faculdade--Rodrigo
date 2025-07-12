def func_verificador(self, escolha):   
            nome_servico, preco = self.servico[escolha]  
            if self.valor >= preco:
                self.valor -= preco
                print(f"\nO cliente {self.nome} pagou o serviço: {nome_servico}, ainda sobrou {self.valor} reais")
            else:
                print(f"\nO cliente {self.nome} não tem dinheiro suficiente para pagar o serviço: {nome_servico}")