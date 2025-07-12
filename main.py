from pacote.classe_veterinario import veterinario

def main():
 nome = input("Digite o seu nome: ")
 servico =  {0: True,
            1: ("vacinação",200),
            2: ("exames", 500),
            3: ("banho e tosa", 150)}
 
 try:
  valor = float(input("Digite o seu valor: "))
  cliente = veterinario(valor, nome, servico)
  escolha = cliente.atendimento()
 except ValueError:
  print("Erro: Digite apenas números para o valor") 
 

 while True: 
  print("")
  print("\n==========Resultado=========")
  print(f"O nome do cliente: {cliente.nome}",
        f"\nO valor: {cliente.valor}")

  if escolha is None:
    break
  elif escolha: 
    cliente.consulta(escolha)
    if cliente.valor >= 0:
     continuar = str(input("\nDeseja continuar o atendimento? (Sim/Não): ")).capitalize()
     if continuar == 'Não':
       print("-----Parando o Petshop------")
       print("")
       break
     elif continuar == 'Sim':
       print("------Continuando o Petshop-------")
       print(f"\nO valor restante é: {cliente.valor}")   
       print("")
       escolha = cliente.atendimento()
     else:
       print("Apenas 'Sim' ou 'Não' são aceitos")
       break       
if __name__ == "__main__":
  main()      