def  func_atendimento(self):
        while True:
         try: 
          print("=======Consulta Veterinária========")
          print("\n1 - vacinação (custa: R$200)",
              "\n2 - exames (custa: R$500)",
              "\n3 - banho e tosa (custa: R$ 150)" 
              "\n0 - sair")  
         
          escolha = int(input("Digite o número entre 0-3: "))
          if escolha < 0 or escolha > 3:
            print("\nErro: Digite apenas números entre 0 até 3!!")
            continue
          elif escolha == 0:
            print("\nAtendimento encerrado")
            return None
          else:
           print(f"\n O serviço escolhido foi {self.servico[escolha][0]}")
           return escolha
         except ValueError:
            print("\nDigite apenas os números correspondentes") 
            continue
