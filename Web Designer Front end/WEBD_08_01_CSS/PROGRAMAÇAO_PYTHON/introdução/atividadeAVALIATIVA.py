
whil
try:
    nome = str(input("Digite seu nome completo: "))
except :
    print("Nome de usuario inválido!")
try:
    idade = int(input("Digite sua idade: "))
except :
    print("Idade digitada inválida!")
try :
    peso = float(input("Digite seu peso em KG: ").replace(",", "."))
except : 
    print("peso digitado invalido")

