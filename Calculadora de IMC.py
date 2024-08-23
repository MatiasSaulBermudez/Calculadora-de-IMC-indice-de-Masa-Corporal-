#Calculadora de IMC (Índice de Masa Corporal):
#•	Pide al usuario que ingrese su peso y altura.
#•	Calcula el IMC utilizando la fórmula: IMC = peso / (altura ** 2).
#•	Muestra el IMC y da un diagnóstico básico (por ejemplo: "Peso bajo", "Normal", "Sobrepeso", "Obesidad").
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f"Su IMC es de: {imc}, su peso esta por debajo del nivel normal")
elif imc >= 18.5 and imc <= 24.9:
    print(f"Su IMC es de: {imc}, Usted tiene un peso normal")
else: 
    print(f"Usted tiene sobrepeso, por favor acuda a un profesional de la salud")
    
