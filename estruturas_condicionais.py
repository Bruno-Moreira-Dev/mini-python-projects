MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade")
else:
    print("Menor de idade")

if idade >= MAIOR_IDADE:
    print("Maior de idade")
elif idade == IDADE_ESPECIAL:
    print("Idade especial")
else:
    print("Menor de idade")
    