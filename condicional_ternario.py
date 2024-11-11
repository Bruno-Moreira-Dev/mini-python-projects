status = "Sucesso"
saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status.upper()} ao realizar o saque!")
