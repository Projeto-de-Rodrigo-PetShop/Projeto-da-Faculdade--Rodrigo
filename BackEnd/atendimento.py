def  func_atendimento(self,selecionar_servico):
    
    # Esta função realiza o atendimento do cliente
    #verifica as condições e assim vai retornar os valores
    
    if  selecionar_servico<0 or selecionar_servico> 4:
        return None
    elif selecionar_servico == 0:
        return 
    elif selecionar_servico in self.servico:
        return selecionar_servico
    else:
        return None
        