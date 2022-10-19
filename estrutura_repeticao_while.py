opcao = -3

while opcao != 0:
    opcao = int(input("[1] sacar \n[2] Extrato \n[0] Sair \n"))
    
    if opcao == 3:
        print("Sacando...")
    elif opcao == 4:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")
    