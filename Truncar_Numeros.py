import math
#com biblioteca math:
num = float(input('Digite um valor decimal: '))

print(f'O valor digitado é {num} e cortado fica:{math.trunc(num)}')

#sem biblioteca:
print(f'O valor {num} truncado fica: {int(num)}')
