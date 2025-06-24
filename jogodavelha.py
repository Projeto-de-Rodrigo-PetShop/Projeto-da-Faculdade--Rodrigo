import os #limpar tela
import random #Número aleatórios
from colorama import Fore, Back, Style #Cores aleatorias e fontes

jogarnovamente="s"
jogadas=0
quemjoga=2
maxjogadas=9
vit='n'

velha = [
     [" "," "," "],
     [" "," "," "],
     [" "," "," "],
]

def tela():
   
    global velha 
    global jogadas
    os.system("cls")
    
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("  ------------ ")
   
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("  ------------")
    
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("  ------------")
    
    print("Jogadas: " + Fore.GREEN + str(jogadas)
           + Fore.RESET)

def jogadorJoga():
    global jogadas
    global quemjoga
    global vit
    global maxjogadas
    if quemjoga == 2 and jogadas < maxjogadas:
        
        try:
         l= int(input("Linha...: "))
         c=int(input("Coluna...: "))
         
         while velha[l][c]!=" ":
            l= int(input("Linha...: "))
            c=int(input("Coluna...: "))
        
            velha[l][c]='X'
            quemjoga=1
            jogadas+=1
       
        except:
            print("Linha e ou coluna inválida")
            os.system("pause")
            #vit="n"


def cpuJoga():
    global jogadas            
    global quemjoga
    global vit
    global maxjogadas
    if quemjoga==1 and jogadas<maxjogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        while velha[l][c]!=" ":
            l=random.randrange(0,3)
            c=random.randrange(0,3)
        velha[l][c]="O"
        jogadas+=1
        quemjoga=2    


while True:
    tela()
    jogadorJoga()
    cpuJoga()