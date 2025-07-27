from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock

from BackEnd.classe_veterinario import veterinario

sistema = veterinario()

#Essa classe vai fazer com que o usuário escolha o método de pagamento

class Comprar (MDScreen):
   servico=None
   
   #Vai determinar os valores que a pessoa colocou
   #E o pagamento que ela vai escolher
   
   def iniciar_pagamento(self, escolha_pagamento):
       
       #Forma mais fácil de escolher o tipo de pagamento, já estando dentro do main.py
       #Não precisando fazer outra chamada para consulta
       #O valor do escolha_pagamento é dado por conta dos botões

        Clock.schedule_once(self.apagar_pagamento, 1) 
        
        if  escolha_pagamento == 1:
            forma_pagamento = "Boleto Bancário"
        elif escolha_pagamento == 2:
            forma_pagamento = "Pix"
        elif escolha_pagamento == 3:
           forma_pagamento = "Cartão de Crédito"
        elif escolha_pagamento == 4:
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
                
                if forma_pagamento in ("Pix", "Boleto Bancário"):
                    self.simular_pagamento_pix(forma_pagamento)
                else:           
                    self.manager.get_screen('verificador').forma_pagamento = forma_pagamento
                    self.manager.get_screen('verificador').verificar(self.servico)
            else:
                self.ids.label_cancelar.text = "Valor Incorreto" 
                return
        else:
            self.manager.current = 'menu'
            self.ids.label_cancelar.text = 'Pagamento cancelado'
   
   #vai simular um pagamento caso o usuario peça por pix 
   
   def simular_pagamento_pix(self, forma_pagamento):   
       
        self.forma_pagamento = forma_pagamento
       
        self.dialog = MDDialog(
        title="QR Code para Pagamento",
        type="custom",
        content_cls=MDBoxLayout(
            Image(source="imagens/codigo_qr-300x300.png"),
            size_hint_y=None,
            height="300dp"
        )
            )
        self.dialog.open()
        self.ids.label_cancelar.text = "Aguardando pagamento..."
        
        Clock.schedule_once(self.pagamento_pix_aprovado, 4)

   def pagamento_pix_aprovado(self, dt):
    
    self.ids.label_cancelar.text = ""

    if hasattr(self, "dialog") and self.dialog:
        self.dialog.dismiss()
        self.dialog = None

    self.manager.get_screen('verificador').forma_pagamento = self.forma_pagamento
    self.manager.get_screen('verificador').verificar(self.servico)
    
   def apagar_pagamento(self,*args):
    self.ids.valores.text = ""
    self.ids.label_cancelar.text = ''

    #----Vai fechar o dialog (hasattr é uma função embutida no python)------

    if hasattr(self, "dialog") and self.dialog:
        self.dialog.dismiss()
        self.dialog = None
    
#Essa Classe vai verificar o pagamento e mandar o resultado

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
         
         if redirecionar_finalizada == True:
            self.manager.current = 'finalizar_compra'
         else:
            self.manager.current = 'menu'
        
        #----Titulo(Dialog) e sua organização----
        
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
                on_release=fechar_nota 
            )
        ]
    )
        self.dialog.open()