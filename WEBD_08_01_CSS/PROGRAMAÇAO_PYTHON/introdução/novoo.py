star = True

while star:
    try: 
        idade = int(input("Digite sua idade em anos " ))
        print("idade digitada corretamente!")
        star = False
    except:
        print("valor informado é inválido!\n")

