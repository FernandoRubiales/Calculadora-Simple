#CALCULADORA BÁSICA - PROYECTO N°1
#Solicitar al usuario 2 numeros y realizar las operaciones correspondientes


#Declaramos las variables
#Utilizamos input para que se guarde lo que el usuario ingresa

num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")

#Realizamos las operaciones y guardamos el resultado
res1 = float(num1) + float(num2)
res2 = float(num1) - float(num2)
res3 = float(num1) * float(num2)
res4 = float(num1) / float(num2)

#Imprimimos el resultado por pantalla
print("La suma es:", res1)
print("La resta es:", res2)
print("La multiplicación es:", res3)
print("La división es:", res4)
