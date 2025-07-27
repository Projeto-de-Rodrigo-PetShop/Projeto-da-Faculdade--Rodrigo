from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from BackEnd.classe_veterinario import veterinario

sistema = veterinario()

class Cadastro(MDScreen):
    
    #função de cadastro, é feito por 2 variáveis (nome_cadastro e senha_cadastro), ambas vão pegar os valores por id
    #Isso quer dizer que o que eu digitar, eles vão receber os valores automaticamente

    def cadastrar(self):
        
        Clock.schedule_once(self.erro_cadastro, 1) 

        nome_cadastro=self.ids.usuario_input.text
        senha_cadastro=self.ids.senha_input.text

        nome_real=self.ids.nome_input.text
        sobrenome_real=self.ids.sobrenome_input.text
        
        if nome_cadastro and senha_cadastro and nome_real and sobrenome_real:

            sistema.cadastro(nome_cadastro, senha_cadastro)
            self.manager.get_screen('login').nome_usuario = nome_cadastro
            self.manager.get_screen('login').senha_usuario = senha_cadastro
            self.manager.current = 'login'
        else:
           self.ids.mensagem_erro.text = "Preencha todos os campos."
    
    def erro_cadastro(self, *args):
        self.ids.mensagem_erro.text = ''    

class Login(MDScreen):
    
    #apenas para declarar as 2 variáveis, que estão vazias, pois ainda não fora comparadas
   
    nome_usuario =""
    senha_usuario = ""
   
    def login(self):
       
        #Vão pegar os valores que eu digitar e compará-los com os antigos
        
        nome_login = self.ids.nome_usuario.text
        senha_login = self.ids.senha_usuario.text
        
        Clock.schedule_once(self.erro_login, 1) 

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

    def erro_login(self, *args):
            self.ids.mensagem_login.text = " "