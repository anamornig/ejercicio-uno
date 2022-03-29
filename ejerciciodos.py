nota_uno= float(input('nota uno: ';))
nota_dos= float(input('nota dos: '))
nota_tres= float(input('nota tres: '))
nota_final= (15* nota_uno + 35* nota_dos + 50*
nota_tres)/100
print('promedio: ' nota_final)

matriz = [
[1, 5, 1],
[2, 1, 2],
[3, 0, 1],
[1, 4, 4]
]
matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))
print(matriz)