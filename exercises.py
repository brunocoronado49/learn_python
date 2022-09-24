print("Hello World!")

var = "Hello World!"
print(var)

name = "Bruno"
print("Hello", name)

result = (((3+2) / (2 * 5)) ** 2)
print(result)

hrs = int(input("Ingresa las horas que trabajas: "))
pay = int(input("Ingresa el pago por hora: "))
total = hrs * pay
print("Tu pago es de", total)

n = int(input("Ingresa un numero positivo: "))
result = n * (n + 1) / 2
print("La suma de todos los enteros de 1 hasta", n, "es:", result)

kg = input("Ingresa tu peso en kg: ")
hg = input("Ingresa tu estatura en metros: ")
imc = round(float(kg)/float(hg) **2, 2)
print("Tu indice de masa corporal es:", float(imc)) 

num_one = int(input("Ingresa un numero entero: "))
num_two = int(input("Ingresa otro numero entero: "))
cos = num_one // num_two
resto = num_one % num_two
print("Entre", num_one, "y", num_two, "cociente:", cos, "y el resto:", resto)

inv = float(input("Ingresa una cantidad a invertir: "))
interes = float("Ingresa el interes anual: ")
year = float(input("Ingresa la cantidad de años: "))
result = round(inv * (interes / 100 + 1) ** year, 2)
print("Capital final:", result)