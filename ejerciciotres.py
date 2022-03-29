#1) Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:


#Mostrar una suma de los dos números
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números
#Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
#En caso de no introducir una opción válida, el programa informará de que no es correcta.


num1 = float(input('ingrese un numero: '))
num2 = float(input('ingrese otro numero: '))
operador = input('elija: suma, resta, multiplicacion o cerrar el programa')

if (operador == 'suma'):
    print(num1 + num2)
elif (operador== 'resta'):
    print(num1 - num2)
elif (operador == 'multiplicacion'):
    print(num1 * num2)
elif (operador == 'cerrar el programa'):
    print('se ha cerrado el programa')
else:
    print('la opcion no es valida')

#2) Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.


cantidad=1

while (cantidad>0) :
    numero = int(input('escriba un numero'))
    if (numero%2):
        print('Ha introducido un numero impar')
        break
    else:
        print('intente de nuevo')



#3) Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:

sum(range(0,101,1))


#4) Escribí un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:

cantidad=int(input('cuantos numeros queres escribir?'))
numero = 0
listadenumeros =[]

while cantidad>numero:
    escrito =int(input('escribi tu numero'))
    numero+=1
    listadenumeros.append(escrito)

print(sum(listadenumeros)/cantidad)


#5) Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

veces=1
numeros = [1, 3, 6, 9]

while veces>0:
    numeroelegido = int(input('escriba un numero entero del 0 al 9: '))
    if numeroelegido>9:
        print('no es correcto, intente de nuevo: ')
    elif numeroelegido in numeros:
        print('esta en la lista')
        break
    else:
        print('no esta en la lista')
        break

#6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

#Todos los números del 0 al 10 [0, 1, 2, ..., 10]
#Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
#Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
#Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
#Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

lista1 = list(range(0,11))
lista2 = list(range(-10,1))
lista3 = list(range(0,21,2))
lista4 = list(range(-19,1,2))
lista5 = list(range(0,51,5))


#6) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

newlista = list(set(lista_1)&set(lista_2))
