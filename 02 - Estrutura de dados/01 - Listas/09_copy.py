lista = [1, "Python", [40, 30, 20]]

backup = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

print(id(backup), id(lista))


lista[0] = 3

print(lista)
print(backup)

backup[1] = "Java"

print(lista)
print(backup)