conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 540

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saldo:
        print("Saque realizado")
    else:
        print("Saldo insuficiente!")