from kivymd.app import MDApp
from kivy.lang import Builder   
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen


from BackEnd.classe_veterinario import veterinario

sistema = veterinario()

Builder.load_file("FrontEnd/telas.kv")
class Gerenciador(ScreenManager):
    pass

class Cadastro(MDScreen):
    
    #função de cadastro, é feito por 2 variáveis (nome_cadastro e senha_cadastro), ambas vão pegar os valores por id
    #Isso quer dizer que o que eu digitar, eles vão receber os valores automaticamente

    def cadastrar(self):

        nome_cadastro=self.ids.nome_input.text
        senha_cadastro=self.ids.senha_input.text
                   
        
        if nome_cadastro and senha_cadastro:

            sistema.cadastro(nome_cadastro, senha_cadastro)
            self.manager.get_screen('login').nome_usuario = nome_cadastro
            self.manager.get_screen('login').senha_usuario = senha_cadastro
            self.manager.current = 'login'
        else:
           self.ids.mensagem_erro.text = "Preencha todos os campos."

class Login(MDScreen):
    
    #apenas para declarar as 2 variáveis, que estão vazias, pois ainda não fora comparadas
   
    nome_usuario =""
    senha_usuario = ""
   
    def login(self, *args ):
       
        #Vão pegar os valores que eu digitar e compará-los com os antigos
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
    def iniciar_atendimento(self, selecionar_servico):

        resultado = sistema.atendimento(selecionar_servico)
         
        #Comparação dependendo do que o usuário escolher
        if resultado is not None:
            self.manager.get_screen('comprar').servico = sistema.servico[selecionar_servico]
            self.manager.current = 'comprar'
        else:
            
                self.manager.current = 'menu'
                self.ids.label_cancelar.text = 'Atendimento cancelado'
                self.ids.label_cancelar.text = ''
class Comprar (MDScreen):
   servico=None
   #Vai determinar os valores que a pessoa colocou
   #E o pagamento que ela vai escolher
   
   def iniciar_pagamento(self, selecionar_servico, escolha_pagamento):
        forma_pagamento = sistema.verificador(selecionar_servico)

       #Forma mais fácil de escolher o tipo de pagamento, já estando dentro do main.py
       #Não precisando fazer outra chamada para consulta
       #O valor do escolha_pagamento é dado por conta dos botões

        if  escolha_pagamento== 1:
            forma_pagamento = "Dinheiro"
        elif escolha_pagamento == 2:
            forma_pagamento = "Pix"
        elif escolha_pagamento == 3:
           forma_pagamento = "Cartão de Crédito"
        elif escolha_pagamento==4:
            forma_pagamento = "Cartão de Débito"
        else:
           self.ids.label_cancelar.text="forma de pagamento inválida"
           return None
        
        if forma_pagamento is not None:
            try:
                sistema.valor = float(self.ids.valores.text)
            except ValueError:
                self.ids.label_cancelar.text = "Digite um valor válido"    
                return         
            self.manager.get_screen('verificador').forma_pagamento = forma_pagamento
            self.manager.get_screen('verificador').verificar(selecionar_servico)
            self.manager.current = 'verificador'
        else:
            self.manager.current = 'menu'
            self.ids.label_cancelar.text = 'Pagamento cancelado'

class Verificador(MDScreen):
    forma_pagamento = None
    def verificar(self, selecionar_servico):
        resultado=sistema.verificador(selecionar_servico) 
       
        #Vai fazer a comparativa com o que a pessoa
        #Caso a pessoa tenha colocado um valor abaixo da do serviço, será insuficiente
        #isinstance verifica se resultado faz parte ou de uma lista ou de uma tupla
        
        if isinstance(resultado,(list,tuple)): 
           
            self.ids.label_verificador.text =  (f"Compra Realizada com Sucesso!\n"
                                               f"O Preço do Serviço: {resultado[2]:.2f}\n"
                                               f"Valor restante: R${resultado[0]:.2f}\n"
                                               f"O Serviço escolhido: {resultado[1]}\n"
                                               f"O Pagamento escolhido: {self.forma_pagamento}")        
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