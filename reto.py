cont = 0
cont2 = 0

while(cont <= 5):
    num = int(input('Digite un numero : '))
    cont += 1
    if (num < 0 ):
        cont2 += 1
    cont+=1   
print(f'El numero de negativos es : {cont2}')
            
        
