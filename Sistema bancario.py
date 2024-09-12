menu = """
=======================
∥ [1] Sacar           ∥ 
∥ [2] Deposito        ∥ 
∥ [3] Extrato         ∥ 
∥ [4] Sair            ∥ 
∥====================== 
"""
#commit
saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUE = 4
numero_saque = 0 

while True:
    opcao = int(input(menu))
    if opcao == 1:
        valor = float(input("digite o valor do saque: "))
        sem_saldo = valor > saldo
        sem_saque = numero_saque > LIMITE_SAQUE
        sem_limite = valor > limite
        if sem_saldo:
            print("Voce nao possui saldo disponivel, porfavor faça um deposito!")
        elif sem_saque:
            print("Voce nao possui saques disponiveis, no maximo 4 por dia!")
        elif sem_limite:
            print("Limite de saque ultrapassado, disponivel apenas 500 reais por operação!!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque valor: R$ {valor:.2f}\n "
            numero_saque += 1
            print ("********SAQUE REALIZADO COM SUCESSO**********")
        else:
            print("operação falha!")
        

    
    elif opcao == 2:
        valor = float(input("Digite o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depoisto: R$ {valor:.2f}\n"
        else:
            print("operação invalida!")

    
    
    elif opcao == 3:
        print("\n*******************EXTRATO*******************") 
        print("SEM MOVIMENTO!!!" if not extrato else extrato)
        print(f"Saldo na conta corrente: R$ {saldo:.2f}") 
        print ("\n**********************FIM***********************")

    elif opcao == 4:
        print("\n*************************************************************")
        print("\nOBRIGADA POR UTILIZAR NOSSOS SERVIÇOS, TENHA UM OTIMO DIA!!!!")
        print("\n*************************************************************")
        break
    else:
        print("Opção escolhida invalida ")