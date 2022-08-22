## Ejercicio 1
# x e y son numeros enteros
# Devuelve el numero mas grande
# Si son iguales, devuleve cualquiera de lso dos 
# Tu codigo:
def obtMayor(x,y):
    if x > y:
        print ('El numero ' + str(x) + ' es el mayor')
    elif y > x:
        print ('El numero ' + str(y) + ' es el mayor')
    else:
        print ('Son iguales')

obtMayor(5555,100000)

mayor = int(input('dame el primer numero: '))
menor = int(input('dame el segundo numero: '))