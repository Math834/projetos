print(2*"-=-="+"-IMC="+2*"-=-=")

altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso/altura**2
print(imc)

if imc<18.5:
    print("Abaixo do peso")

elif 18.5>imc>24.9:
    print("Peso normal")

elif 25>imc>29.9:
    print("Excesso de peso")

elif 30>imc>35:
    print("Obesidade")

else:
    print("Obesidade extrema")