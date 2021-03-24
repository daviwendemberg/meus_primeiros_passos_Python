import math

ang = float(input('digite o angulo: '))#repassar o angulo

seno = math.sin(math.radians(ang))#definindo uma variavel com o seno

coss = math.cos(math.radians(ang))#definindo uma variavel com o cosseno

tan = math.tan(math.radians(ang))#definindo uma variavel com a tangente
#esse print aqui vai exibir o resultado do calculo na tela
print(f'O ângulo de {ang} tem o seno={seno:.2f} \n o ângulo de {ang} tem o cosseno={coss:.2f} \n o ângulo de {ang} tem o  tangente={tan:.2f}')
