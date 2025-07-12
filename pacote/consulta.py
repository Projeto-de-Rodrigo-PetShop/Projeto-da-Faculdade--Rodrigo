
def func_consulta(self,escolha):
      while True:
         try:     
           print("\n=======Formas de Pagamento========")
           print("\n1 - Dinheiro",
                 "\n2 - Cartão de crédito",
                 "\n3 - Cartão de débito",
                 "\n4 - Pix",
                 "\n0 - Sair")
         
           forma_pagamento = int(input("Digite o número entre 0-4: "))
           
           if forma_pagamento< 0 or forma_pagamento > 4:
            print("\nErro: Digite apenas números entre 0 até 4!!")
            continue
           elif forma_pagamento == 0:
            print("\nPagamento interrompido") 
            return None
           else:
            print(f"\nO pagamento será feito por: {self.pagamento[forma_pagamento][0]}")           
            return forma_pagamento
         except ValueError:
            print("\nErro: Digite apenas os números correspondentes") 
            continue    