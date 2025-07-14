from kivymd.app import MDApp
from kivy.lang import Builder   
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton


from BackEnd.classe_veterinario import veterinario

sistema = veterinario()

Builder.load_file("FrontEnd/telas.kv")
class Gerenciador(ScreenManager):
    pass

class Cadastro(MDScreen):
    
    #função de cadastro, é feito por 2 variáveis (nome_cadastro e senha_cadastro), ambas vão pegar os valores por id
    #Isso quer dizer que o que eu digitar, eles vão receber os valores automaticamente

    def cadastrar(self):
       
        nome_cadastro = self.ids.nome_input.text
        senha_cadastro = self.ids.senha_input.text

        #condição que pede tanto a senha quanto cadastro para prosseguir 
        if nome_cadastro and senha_cadastro:

            #Vai armazenar as 2 variáveis dentro da classe veterinario e retornarão na função cadastro
            sistema.cadastro(nome_cadastro, senha_cadastro)
            self.manager.get_screen('login').nome_usuario = nome_cadastro
            self.manager.get_screen('login').senha_usuario = senha_cadastro
            self.manager.current = 'login'
        else:
           self.ids.mensagem_erro.text = "Preencha todos os campos."

class Login(MDScreen):
    #apenas para declarar as 2 variáveis, que estão vaziar, pois ainda não fora comparadas
    nome_usuario = ""
    senha_usuario = ""
    def login(self, *args ):
        #Vão pegar os valores que eu digitar 
        nome_login = self.ids.nome_usuario.text
        senha_login = self.ids.senha_usuario.text
        #chamada da classe para pegar as variáveis, levando em conta as variáveis dentro da classe veterinario
        sistema.nome = nome_login
        sistema.senha = senha_login
        
        #variável para armazenamento e comparação com o que está na função cadastro(BackEnd)
        logado = sistema.salvar_login(nome_login, senha_login)
        if logado: 
            
            self.ids.mensagem_login.text = "Login bem-sucedido!"
            self.manager.current = 'menu'
            self.manager.get_screen('menu').Montar_Perfil()
        else:
            self.ids.mensagem_login.text = "Senha ou nome de usuário incorretos."
         
class Menu(MDScreen):
    #Apenas para mostrar o nome do usuário e levar esse valor para a tela de menu
    def Montar_Perfil(self):
        #o .get_screen('') é o comando q leva tal informação para outra tela
        nome_usuario = self.manager.get_screen('login').nome_usuario
        sistema.nome = nome_usuario
        self.ids.label_nome.text =  f'Nome do Usuário: {nome_usuario}'
        
class Atendimento(MDScreen):
    

    def meus_servicos(self):
        self.ids.texto.text = "Serviços disponíveis:\n"

        servicos = {1:("Vacinação", 200),
                    2:("Exames",500),
                    3:("Banho e tosa", 150)}
        
        #Vai pegar todas as keys(números) e os values, passando-os e os adicionando na tela
        for key, value in servicos.items():
            label1= MDLabel(text= (f"{key} - {value} (custa: R${value[1]})"))
            self.ids.box_servicos.add_widget(label1)

    def iniciar_atendimento(self, escolha):

        #vai pegar as condicionais que há na função atendimento
        resultado = sistema.atendimento(escolha)
         
        #Comparação dependendo do que o usuário escolher
        if resultado is not None:
            self.manager.get_screen('comprar').servico = sistema.servico[escolha]
            self.manager.current = 'comprar'
        else:
            
                self.manager.current = 'menu'
                self.ids.label_cancelar.text = 'Atendimento cancelado'
                self.ids.label_cancelar.text = ''
    
class Comprar (MDScreen):
   servico=None
   def modos_pagamentos(self):
    
    tipos_de_pagamento = {
       1: "Dinheiro",
       2: "Cartão de crédito",
       3: "Cartão de débito",
       4: "Pix"}
    
    self.ids.label_pagamento.text = "Formas de Pagamento:\n"
    for key, value in tipos_de_pagamento.items():
        label2 = MDLabel(text=f"{key} - {value[0]}", halign="left")
        self.ids.box_comprar.add_widget(label2)
       

   #Vai determinar os valor que a pessoa colocou
   #E o pagamento que ela vai escolher
   def iniciar_pagamento(self, servico,escolha):
        forma_pagamento = sistema.consulta(escolha)
       
        if forma_pagamento is not None:
            try:
                self.saldo = float(self.ids.valores.text)
            except ValueError:
                self.ids.label_cancelar.text = "Digite um valor válido"    
                return         
            sistema.saldo = self.saldo

            self.manager.get_screen('verificador').forma_pagamento = forma_pagamento
            self.manager.get_screen('verificador').verificar(servico)
            self.manager.current = 'verificador'
        else:
            self.manager.current = 'menu'
            self.ids.label_cancelar.text = 'Pagamento cancelado'

class Verificador(MDScreen):
    forma_pagamento =None
    def verificar(self, selecionar_servico):
        resultado=sistema.verificador(selecionar_servico) 
        forma_pagamento_processo = self.forma_pagamento 

        #Vai fazer a comparativa com o que a pessoa
        #Caso a pessoa tenha colocado um valor abaixo da do serviço, será insuficiente
        #isinstance verifica se resultado faz parte ou de uma lista ou de uma tupla
        
        if isinstance(resultado,(list,tuple)): 
            self.ids.label_verificador.text =  f"Compra Realizada com Sucesso!\n"
            self.ids.label_verificador.text =  f"O Preço do Serviço: {resultado[2]:.2f}\n"
            self.ids.label_verificador.text =  f"Valor restante: R${resultado[0]:.2f}\n"
            self.ids.label_verificador.text =  f"O Serviço escolhido: {resultado[1]}\n"                       
            self.ids.label_verificador.text = f"O Pagamento escolhido foi: {forma_pagamento_processo[0]}\n"        
        else:
            self.ids.label_verificador.text = f"{resultado}"
       
class FinalizarCompra(MDScreen):
    
    
    pass
class Executador_App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"
        return Gerenciador()
    
if __name__ == '__main__':
    Executador_App().run()    