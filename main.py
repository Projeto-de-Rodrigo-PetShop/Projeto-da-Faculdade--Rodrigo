from kivymd.app import MDApp
from kivy.lang import Builder   
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel


from KivyMD import *

from BackEnd.classe_veterinario import veterinario

sistema = veterinario()

Builder.load_file("FrontEnd/telas.kv")
class Gerenciador(ScreenManager):
    pass
class Comprar (MDScreen):
   servico=None
   
   #Vai determinar os valores que a pessoa colocou
   #E o pagamento que ela vai escolher
   
   def iniciar_pagamento(self, escolha_pagamento):
       
       #Forma mais fácil de escolher o tipo de pagamento, já estando dentro do main.py
       #Não precisando fazer outra chamada para consulta
       #O valor do escolha_pagamento é dado por conta dos botões

        Clock.schedule_once(self.apagar, 1) 
        
        if  escolha_pagamento== 1:
            forma_pagamento = "Boleto Bancário"
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
                return  None    
            
            if sistema.valor > 0:         
                self.manager.get_screen('verificador').forma_pagamento = forma_pagamento
                self.manager.get_screen('verificador').verificar(self.servico)
            else:
                self.ids.label_cancelar.text = "Valor Incorreto" 
                return
        else:
            self.manager.current = 'menu'
            self.ids.label_cancelar.text = 'Pagamento cancelado'
   
   def apagar(self,*args):
    self.ids.valores.text = ""
    self.ids.label_cancelar.text = ''

class Verificador(MDScreen):   
    dialog = None
    forma_pagamento = None
    def verificar(self, servico):
        resultado=sistema.verificador(servico) 
       
        #Vai fazer a comparativa com o que a pessoa
        #Caso a pessoa tenha colocado um valor abaixo da do serviço, será insuficiente
        #isinstance verifica se resultado faz parte ou de uma lista ou de uma tupla
        
        if isinstance(resultado,(list,tuple)): 
           
            self.ids.label_verificador.text =  (f"Compra Realizada com Sucesso!\n"
                                               f"O Preço do Serviço: {resultado[2]:.2f}\n"
                                               f""
                                               f"Valor restante: R${resultado[0]:.2f}\n"
                                               f""
                                               f"O Serviço escolhido: {resultado[1]}\n"
                                               f""
                                               f"O Pagamento escolhido: {self.forma_pagamento}")        
        
            texto = self.ids.label_verificador.text
            cor = (0,0.5,0.5,1)
            redirecionar_finalizada = True
        else:
            texto = f"{resultado}"
            cor =(1,0,0,1)
            redirecionar_finalizada = False
        
        self.nota_fiscal(texto, cor, redirecionar_finalizada)   

    #Essa função vai fazer com que a nota fiscal seja mostrada após a realização de um pagamento
    #quando apertado no botão 'OK' você será redirecionado ao finalizar_compra

    def nota_fiscal(self, texto, cor, redirecionar_finalizada = False):   
        def fechar_nota(x):
         self.dialog.dismiss()
         
         #Forma de comparar as respostas e enviar o usuário para o menu ou não
         if redirecionar_finalizada == True:
            self.manager.current = 'finalizar_compra'
         else:
            self.manager.current = 'menu'
        
        #Todo o título e a sua customização

        self.dialog = MDDialog(
          title="Resultado da Compra",
          type="custom",
          radius=[20, 7, 20, 7],
          md_bg_color=cor,
          content_cls=MDLabel(
            text=texto,
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            size_hint_y=None
        ),
        buttons=[
            MDRaisedButton(
                text="Finalizar",
                text_color=(1, 1, 1, 1),
                on_release=fechar_nota #Botão que vai fazer a chamada da função
            )
        ]
    )
        self.dialog.open()
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