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

# Saber si un elemento existe en una lista
print("pink" in colors)

# Añadiendo un nuevo elemento a lista
colors.append("pink")
print(colors)
print("pink" in colors)

# Agregar más de un elemento a una lista
colors.extend(["yellow", "violet"])
print(colors)

# Agregar un color en cierta posicion
colors.insert(1, "black")
print(colors)

# Quitar el ultimo elemento de la lista
colors.pop()
print(colors)

# Quitar un elemento de la lista con un parametro
colors.remove("red")
print(colors)

# Para eliminar todos los elementos de la lista
colors.clear()
print(colors)

# Ordenar los elementos de un array
order = ["c", "a", "b", "d", "z", "y", "k"]
order.sort()
print(order)
order.sort(reverse=True)
print(order)