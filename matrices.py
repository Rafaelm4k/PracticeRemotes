import random as r
print("Generar Matriz Bidimensional")

matriz = []

for i in range(5):
	matriz.append([])
	for j in range(5):
		matriz[i].append(r.randint(1,9))
for fila in matriz:
	print(fila)


