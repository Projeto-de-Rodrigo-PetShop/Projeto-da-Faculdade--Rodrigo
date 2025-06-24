class Aluno:
  def __init__ (self,matricula, notas):
    self.matricula=matricula
    self.notas= notas

  def Media(self):

    
    media = self.notas/3
    print(f'A sua média foi: {media}')
    if media > 10:
       print(f'Media Aritmetica incongruente!!!')
       return
    elif media >= 7 and media <= 10:
     print(f"O aluno {self.matricula} foi Aprovado!")
    else: 
     print(f"O aluno {self.matricula} foi Reprovado!")

matricula=input("Digite a sua matrícula")
n1= int(input("Digite a sua nota: "))
n2= int(input("Digite a sua nota: "))
n3= int(input("Digite a sua nota: "))
notas= n1+n2+n3

minha_media=Aluno(matricula, notas)
minha_media.Media()