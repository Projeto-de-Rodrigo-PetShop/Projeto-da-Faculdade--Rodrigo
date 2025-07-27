from kivymd.uix.screen import MDScreen
from BackEnd.classe_veterinario import veterinario

sistema = veterinario()

class Menu(MDScreen):
    
    #Apenas para mostrar o nome do usuário e levar esse valor para a tela de menu
   
    def Montar_Perfil(self):
        
        #O .get_screen('') é o comando q leva tal informação para outra tela
        
        nome_usuario = self.manager.get_screen('login').nome_usuario
        sistema.nome = nome_usuario
        self.ids.label_nome.text =  f'Nome do Usuário: {nome_usuario}'