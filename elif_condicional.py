opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato\nEscolha uma opção: "))

if opcao == 1:
    print("Sacar")
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")