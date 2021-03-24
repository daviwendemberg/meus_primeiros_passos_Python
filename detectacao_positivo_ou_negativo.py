import math

variavel1 = int(input('Me passe um numero para descobrir se o mesmo é positivo ou negativo: '))

if(variavel1 >= 1):
    print(variavel1, 'é positivo')
elif(variavel1 == 0):
    print('este valor é neutro')
else:
    print(variavel1, 'é negativo')
