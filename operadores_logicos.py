saldo = 1000
saque = 200
limite = 100

compare_saldo_and = saldo >= saque and saque <= limite
compare_saldo_or = saldo >= saque or saque <= limite
compare_saldo_not = not (saldo > saque)

print(f'AND: {compare_saldo_and}')
print(f'OR: {compare_saldo_or}')
print(f'NOT: {compare_saldo_not}')

print(True and False)
print(True or False)
print(not True)
