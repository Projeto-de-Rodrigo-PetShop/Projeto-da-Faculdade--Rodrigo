from pacote.classe_veterinario import veterinario

def main():
 #Variáveis iniciais
 nome = input("Digite o seu nome: ")
 
 servico =  {0: True,
            1: ("vacinação",200),
            2: ("exames", 500),
            3: ("banho e tosa", 150)}
 
 pagamento={0: True,
          1: ("dinheiro",0),
          2: ("cartão de crédito",0),
          3: ("cartão de débito",0),
          4: ("pix",0)}
 
 try:
  valor = float(input("Digite o seu valor: "))
  cliente = veterinario(valor, nome, servico, pagamento)
  escolha = cliente.atendimento()
 except ValueError:
  print("Erro: Digite apenas números para o valor") 
 
 #Foi retirado a codificação que faz o programa parar caso o usuário queira
 #E ainda será feito a organização do código (loop) sobre os "If's" e "Elif's"
 
 while True: 
  print("")
  if escolha is None:
    break
  elif escolha: 
    if cliente.valor < 0:
      print("\nO valor não pode estar negativado")
      break
    else:
      forma_pagamento=cliente.consulta(escolha) 
      if forma_pagamento is None:
        break
      elif forma_pagamento:
        print("\n==========Resultado=========")
        print(f"O nome do cliente: {cliente.nome}",
        f"\nO valor: {cliente.valor}",
        f"\nO tipo de pagamento: {cliente.pagamento[forma_pagamento][0]}")
        print("============================")
        cliente.verificador(forma_pagamento)
        print("\n-----Atendimento finalizado-----")
        print("")
        break
if __name__ == "__main__":
  main()      