
# funções
valor = "aula POO 26/04/23"
print(valor)

# função print2
def print2(valor_entrada):
  print(valor_entrada)
  
# função print3
def print3(valor_entrada):
  return valor_entrada + 1

valor1 = "POO"
valor2 = 1
print2(valor1)
print(print3(valor2))

def calculo_media():
  valor1 = int(input("informe o valor 1: "))
  valor2 = int(input("informe o valor 2: "))
  media = (valor1 + valor2)/2
  print(media)
  return media