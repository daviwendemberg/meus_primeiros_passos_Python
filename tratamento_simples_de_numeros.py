num = int(input('Me passe um valor de 0 a 9999: '))
u = num / 1 % 10
d = num / 10 % 10
c = num / 100 % 10
m = num / 1000 % 10
print(f'\n {m:.0f} é a milhar \n {c:.0f} é a centena \n {d:.0f} é a dezena \n {u:.0f} é a unidade ')
