demo_list = [1, "Hello", 2.43, True, [1, 2, 3]]
print(demo_list)

# Constructor, solo espera una propiedad
number_list = list((1, 2, 3, 4))
print(type(number_list))
print(number_list)

# Basado en un rango, crea una lista
rang = list(range(1, 20))
print(rang)

# Obtiene metodos de una lista
colors = ["red", "blue", "green"]
print(colors)
print(dir(colors))
print(len(colors))
print(colors[2])