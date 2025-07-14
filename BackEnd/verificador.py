def func_verificador(self, selecionar_servico):   
    
    #Está função verifica se o cliente tem saldo suficiente para pagar pelo serviço
    
    nome_servico, preco = self.servico[selecionar_servico]
    if self.valor <=0:
        return f"Não pode ser Zero e Nem valores Abaixo"
    elif self.valor >= preco:
        self.valor -= preco

        #Esse return vai retornar as variáveis em lista, ou em tupla
        return self.valor, nome_servico, preco
    else:
        return f"Valor insuficiente para o serviço {nome_servico}. Preço: R${preco}, seu saldo: R${self.valor}."