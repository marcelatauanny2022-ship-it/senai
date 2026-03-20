start = True
campo = 1 
 
while start:
     match campo:
          case 1: 
                try:
                    nome = input("Qual e o seu nome?")
                    campo += 1 
                except:
                    print("Escreva o seu nome correto!")
                
                try: 
                    idade = int(input("Qual e a sua idade?"))
                    if idade < 20:
                        print("Programa permitido apenas para maiores de 20 anos!")
                    
                    campo += 1 
                except: 
                
                    print("Por favor! Digite a idade com apenas numeros1")

          case 3: 
                try:
                    peso = float(input("Qual e o seu peso (Kg)? ").replace(",","."))
                    campo += 1 
                except:
                    print("Valor inválido! Digite o peso usando número." )
            
          case 4:
                try:
                    altura= float(input("Digite qual e a sua altura").replace(",","."))
                    campo += 1
                except:
                    print("Altura inválida!")

imc = peso / (altura ** 2)
if idade >= 20 and idade <=60:
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Classificação: Peso normal") 
    elif imc >= 25 and imc <= 29.99:
        print("Classificação: Sobre o peso")
    else:
        imc = "Obesidade"

else:
    if imc <22:
        imc = "Baixo Peso"
    elif imc >= 22 and imc <= 27:
        imc = "Peso normal"
    elif imc >= 25 and imc <= 29.99:
        imc = "Sobre o peso"
    else:
        imc = "Obesidada" 

print("Seu nome", nome)
print("idade", idade)
print("peso", peso)
print("altura", altura)

print("Deseja finalizar o programa?\n")
corfirma= str(input("Digite S (Finalizar) ou N (iniciar)"))
    
if corfirma == "S" or corfirma == "s":
    inicio = False
    print("Obrigado por utilizar o programa")
else:
    print("Opção inválida...")
     
