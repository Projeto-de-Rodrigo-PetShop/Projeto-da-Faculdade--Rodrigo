from kivymd.app import MDApp
from kivy.lang import Builder   
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window

from KivyMD import *

from BackEnd.classe_veterinario import veterinario

sistema = veterinario()

Builder.load_file("FrontEnd/telas.kv")
class Gerenciador(ScreenManager):
    pass
class FinalizarCompra(MDScreen):
    pass
class Executador_App(MDApp):
    def build(self):
        
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 1
        
        return Gerenciador()
    
    def modo_escuro(self):
        
        if self.theme_cls.primary_palette =="Teal":
            self.theme_cls.primary_palette = "Orange"
        else:
            self.theme_cls.primary_palette ="Teal"
        
        if self.theme_cls.theme_style== "Light":
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"
    
if __name__ == '__main__':
    Window.size = (400,600)
    Executador_App().run()    