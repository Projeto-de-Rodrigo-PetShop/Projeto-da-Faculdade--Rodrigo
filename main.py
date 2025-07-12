from pacote.classe_veterinario import veterinario

def main():
 nome = input("Digite o seu nome: ")
 servico =  {0: True,
            1: ("vacinação",200),
            2: ("exames", 500),
            3: ("banho e tosa", 150)}
 
 try:
  valor = float(input("Digite o seu valor: "))
  cliente = veterinario(valor, nome,servico)
  print("")
  print("\n==========Resultado=========")
  print(f"O nome do cliente: {cliente.nome}",
        f"\nO valor: {cliente.valor}")
   
  escolha = cliente.atendimento()
  if escolha: 
   cliente.consulta(escolha)
 except ValueError:
   print("\nError - Apenas números são aceitos -")

if __name__ == "__main__":
  main()