my_str = "Hello World"

# Muestra todos los metodos o propiedades por consola
print(dir(my_str))

# Convierte todo a mayusculas
print(my_str.upper())

# Convierte todo a minuscula
print(my_str.lower())

# Cambia las letras dependiendo de como esten
print(my_str.swapcase())

# Remplaza una palabra por otra en el string
new_str = my_str.replace("World", "Bruno")
print(new_str)

# Cuenta los caracteres en un string
char = my_str.count("o")
print(char)

# Muesrta si empieza con la palabra indicada
start = my_str.startswith("Bruno")
print(start)

# Separa las palabras de un string basado en los espacios
all_wrds = "Hola esta es una variable para separar"
words = all_wrds.split()
print(words)

# Muestra por consola el número del indice del caracter en un string
index = my_str.index("o")
print(index)

# Muestra la longitud del string
length = len(my_str)
print(length)

# Muestra si el string es numérico
num = my_str.isnumeric()
print(num)

# Muestra la posición del caracter
pos = my_str[4]
print(pos)