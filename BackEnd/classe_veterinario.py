
from .atendimento import func_atendimento
#from .consulta import func_consulta
from .verificador import func_verificador

class veterinario:
    def __init__(self):
       
       #Tive que tirar as variáveis do parâmetro da função init, pois tinham 5 parâmetros
       #Isso impedia que eu chamasse a classe para alguma função na hora de juntar o BackEnd com o FrontEnd

        self.valor = 0
        self.nome = ""
        self.servico = {1: ("Vacinação", 200),
                        2: ("Exames", 500),
                        3: ("Banho e tosa", 150),
                        4: ("Adestramento", 350)}
        
        self.pagamento = {1: "Dinheiro",
                         2: "Cartão de crédito",
                         3: "Cartão de débito",
                         4: "Pix"}
        self.senha = ""
        self.cliente={}

    #utilização do "self.cliente" para a realização do cadastro, pois assim ele vai guardar o nome
    #Quando é um dicionário, ele pode guardar mais de 1-2 valores diferentes, formando uma (key: value) --> items

    def cadastro(self, nome, senha):
        if nome in self.cliente:
            return "Usuário já cadastrado"
        #Vai comparar a key (nome) com o seu determinado value(senha)
        self.cliente[nome]= senha
        return f"Cadastro feito!"  
    def salvar_login(self, nome, senha):
       
       #Vai pegar o que tem dentro do dicionário e fazer a comparativa
       #Assim evitando que uma key/nome diferente peguem numa mesma senha
       if self.cliente.get(nome) == senha:
           self.nome=nome
           self.senha=senha
           
           #True para poder passar para a próxima tela quando o botão for acionado
           return True
       #False para não passar para a próxima tela quando o botão for acionado
       return False
    
    def  atendimento(self, selecionar_servico):
        return func_atendimento(self, selecionar_servico)
    
    def verificador(self, selecionar_servico):
        return func_verificador(self, selecionar_servico)