from random import randrange

print(3*"-=-="+"-Adivinhe o número="+3*"-=-=")
def print_com_linha(mensaguem):
    print(mensaguem)
    print(7*"______")

numero = randrange(1, 20)
tentativa = 0
pontos_dica = 0
resposta_dica = None

print("\nTente adivinhar o número de 1 a 20. Boa sorte!!\n")

while True:
    try:
        resposta = int(input("-Qual a sua resposta? "))
        print()

        if resposta == 99:
            break

        if resposta == numero:
            print_com_linha("Parabéns!!! Você acertou!")
            break

        elif resposta > numero:
            print_com_linha("Por favor, digite um número de 1 a 20")

        else:
            print_com_linha("Você errou. Tente de novo.")
            tentativa+=1
    except:
        print_com_linha("\nPor favor, digite apenas números")
        
    if tentativa >= 3:
        while resposta_dica != "n":
            if pontos_dica == 2:
                break

            resposta_dica = input("Você quer uma dica?[s/n] ")

            if resposta_dica == int  or resposta_dica != "n" and resposta_dica != "s":
                print('Pro favor, use apenas "s" ou "n".')

            if resposta_dica == "n":
                print_com_linha("ok. Boa sorte!")

            if resposta_dica == "s":
                pontos_dica+=1

                if pontos_dica == 1:
                    dica = numero % 2
                    
                    if dica == 1:
                        print_com_linha("-É um número ínpar.")

                    else:
                        print_com_linha("-É um número par.")
                    break

                elif pontos_dica == 2:
                    if numero >= 10:
                        print_com_linha("É número de 2 digitos.")

                    else:
                        print_com_linha("É um número de 1 digito.")
                    break
