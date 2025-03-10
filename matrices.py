import random as r
print("Generar Matriz Bidimensional")

Matriz = []

for i in range(3):
	Matriz.append([])
	for j in range(3):
		Matriz[i].append(r.randint(1,9))


for fila in Matriz:
	print(fila)


