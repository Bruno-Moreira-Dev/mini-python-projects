# FOR LOOP

# texto = input("Informe um texto: ")
# VOGAIS = "AEIOU"

# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end="")
# else:
#     print() # adiciona quebra de linha
#     print("Executa no final do laço")

# for numero in range(0, 11):
#     print(numero, end=" ")
# else:
#     print()

# for numero in range(0, 51, 5):
#     print(numero, end=" ")

# WHILE LOOP
# opcao = -1

# while opcao != 0:
#     opcao = int(input("Informe uma opção: \n[0] Sair\n[1] Sacar \n[2] Extrato\nEscolha uma opção: "))

#     if opcao == 1:
#         print("Sacar")
#     else:
#         print("Exibindo o extrato...")
# else:
#     print("Obrigado por utilizar o sistema!")

# FOR CONTINUE
# for numero in range(100):
#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")

# WHILE CONTINUE-BREAK
while True:
    numero = int(input("Informe um numero: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue


    print(numero)