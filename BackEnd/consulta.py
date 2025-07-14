
def func_consulta(self,escolha):
        
      #.get serve para pegar um valor dentro de um dicionário
      # Esta função verifica a forma de pagamento escolhida pelo cliente
   self.forma_pagamento = escolha
   pagamento = {
         1: "Dinheiro",
         2: "Cartão de crédito",
         3: "Cartão de débito",
         4: "Pix"}
      

   if self.forma_pagamento == 1:
      return pagamento[1]
   elif self.forma_pagamento == 2:
      return pagamento[2]
   elif self.forma_pagamento == 3:
      return pagamento[3]
   elif self.forma_pagamento==4:
      return pagamento[4]
   else:
      return "forma de pagamento inválida"
