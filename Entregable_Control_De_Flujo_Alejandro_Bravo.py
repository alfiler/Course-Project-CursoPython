#Ejercicio 1
 
# resultado = 0
# numero1 = 0
# numero2 = 0 
# menu = 0

# while menu != 4:
#     menu = int(input('Elija alguna de las siguientes opciones: \n 1.- Ingresar y sumar 2 numeros \n 2.- Ingresar y restar 2 numeros \n 3.- Ingresar y multiplicar 2 numeros \n 4.- Salir \n'))
    
#     if menu <= 3:

#         numero1 = int(input('Ingrese el primer valor: '))
#         numero2 = int(input('Ingrese el segundo valor: '))

#         if menu == 1:

#             resultado = numero1 + numero2
#             print('El resultado de la suma es ' + str(resultado)+ '\n')
           
#         if menu == 2:
           
#             resultado = numero1 - numero2
#             print('El resultado de la resta es ' + str(resultado)+'\n')
           
#         if menu == 3: 
           
#             resultado = numero1 * numero2
#             print('El resultado de la multiplicacion es ' + str(resultado) + '\n')
           
#         print('Vuelva a ingresar una opcion \n')
#     elif menu > 4:
#         print('Valor Incorrecto, por favor ingrese alguno de los valores del menu')

# print('Selecciono la opcion 4, usted ha salido del programa.')
    
#Ejercicio 2

# numero1 = 0
# divisor = 2
# modulo = 0

# while modulo == 0:
#     numero1 = int(input('Introduzca un numero impar: '))

#     modulo = numero1 % divisor

#     if modulo == 0 :
#         print('El numero ingresado fue: ' + str(numero1) + '\n Vuelva a introducir un valor')

# print('Gracias por ingresar un numero impar.')

#Ejercicio 3

# resultado =  sum(range(1,100,2))

# print('El resultado de los numeros impares entre 0 y 100 es: ' + str(resultado))

#Ejecicio 4

# cantidadN = 0
# suma = 0
# sumador = 0
# x = 0

# cantidadN = int(input("Cuantos numeros desea ingresar: "))

# for x in range(cantidadN): 
#     suma = int(input("Ingrese un numero: "))

#     sumador += suma
#     x +1

# suma = sumador / cantidadN

# print ("La media es:" + str(suma))


# Ejercicio 5

# numeros = [1, 3, 6, 9]

# numero1 = 0
# control = False

# while control != True :
#     numero1 = int(input("Ingrese un valor entre 0 - 9: "))
#     if numero1 <= 9:
#         if numero1 in numeros :
#             control = True
#     else: 
#             print("Valor incorrecto.\n")
# print("Valor ingresado correcto")


# Ejercicio 6

# lista1 = list(range(0,11,1))
# print(lista1)

# lista2 = list(range(-10,1,1))
# print(lista2)

# lista3 = list(range(0,21,2))
# print(lista3)

# lista4 = list(range(-19,1,2))
# print(lista4)

# lista5 = list(range(0,51,5))
# print(lista5)


# Ejercicio 7

# lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
# lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

# lista3 = list(set(lista_1 + lista_2))
# print(lista3)