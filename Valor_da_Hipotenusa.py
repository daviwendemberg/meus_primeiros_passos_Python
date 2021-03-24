'''
#esse algoritmo aqui, eu fiz sem bibliotecas

oposto = float(input('Qual valor do cateto oposto? '))
adjacente = float(input('Qual valor do cateto adjacente? '))
hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)
print(f'o valor do cateto oposto ao quadrado mais o cateto adjacente ao quadrado é igual ao valor da hipotenusa: {hipotenusa:.2f}')
'''
#aqui eu utilizei a biblioteca math, para mostrar duas formas de se utilizar o mesmo algoritmo
import math

co = float(input('catoto oposto: '))
ca = float(input('cateto adjacente: '))
hip = math.hypot(co,ca)
print(f'o valor da hipotenusa: {hip:.2f}')
