import math
#MENU DE OPCIONES

opc = 1


print('EMPANADAS EL MACHETICO')
print('-----------|------------')
print('0. Salir')
print('1. Encontar multiplo del 2')
print('2. Encontar raiz cuadrada')
print('3. Sumar +1000')
print('4. Elevar a la 2')

while(opc != 0):
    opc = int(input('Digita una opcion :'))
    if(opc ==1):
        num = int(input('Digite un numero entero : '))
        if(num % 2 == 0 and num != 0 and num > 0):
            print(f'El numero {num} es multiplo de 2')
        else:
            print(f'El numero {num}  no es multiplo de 2')
    elif(opc == 2):
        num = int(input('Digite un numero entero : '))
        print(f'La raiz cuadrada de {num} es : {math.sqrt(num)}')
    elif(opc == 3):
        num = int(input('Digite un numero entero : '))
        print(f'La suma de {num} es : {num + 100}')
    elif(opc == 4):
        num = int(input('Digite un numero entero : '))
        print(f'El cuadrado de el numero {num} es : {num * num}')
    elif(opc == 0):
        break    
    else :
        print(f'La opcion {opc} no existe, digita una opcion valida')
        print('Digita una opcion valida del 1 al 4 :')           
else:
    print('Parar')    