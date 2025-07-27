from BackEnd.classe_veterinario import veterinario
from kivymd.uix.screen import MDScreen

sistema = veterinario()

#Essa Classe vai fazer o atendimento dos serviços

class Atendimento(MDScreen):
    def iniciar_atendimento(self, selecionar_servico):

        resultado = sistema.atendimento(selecionar_servico)
         
        #Comparação dependendo do que o usuário escolher
        
        if resultado is not None:
            self.manager.get_screen('comprar').servico = selecionar_servico
            self.manager.current = 'comprar'
        else:
            
                self.manager.current = 'menu'
                self.ids.label_cancelar.text = 'Atendimento cancelado'
                self.ids.label_cancelar.text = ''