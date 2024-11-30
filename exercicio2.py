
print("----------Bem Vindo a marmitaria da Yasmin Fioramonte----------")# nome impresso
print(" ")
print('----------------------------MENU-------------------------------')# apresenta o menu de opções, tamanhos e preços
print("---------------------------------------------------------------")
print('----| Tamanho | Bife Acebolado (BA) | Filé de Frango (FF) |----')# A presenta opções e o indice de tamanho
print("----|    P    |      R$ 16.00       |     R$ 15.00        |----")# Opções de preços das marmitas do tamnho P
print("----|    M    |      R$ 18.00       |     R$ 17.00        |----") # Opções de preços das marmitas do tamnho M
print("----|    G    |      R$ 22.00       |     R$ 21.00        |----") # Opções de preços das marmitas do tamnho G
print("---------------------------------------------------------------")
print('')

total = 0

while True:# loop
    sabor = input("Digite o sabor da marmita (BA , FF): ").upper()# entra com o sabor da marmita
    if (sabor != "BA") and ( sabor != "FF"):#opção caso usuário digite valor diferente de BA , FF
        print("Sabor inválido. Tente novamente")
        continue

    tamanho = input("Digite o tamanho da marmita (P , M , G): ").upper()# entra com tamamho da marmita
    if (tamanho != "P") and (tamanho != "M") and (tamanho != "G"):# opção caso usuário digite algo diferente de P, M , G
        print("Tamanho inválido. Tente novamente")
        continue

    if sabor == "BA":# opção de tamanhos e preços BA
        if tamanho == "P":
            preco = 16
        elif tamanho == "M":
            preco = 18
        elif tamanho == "G":
            preco = 22

    elif sabor == "FF":# opção de tamanhos e preços  FF
        if tamanho == "P":
            preco = 15
        elif tamanho == "M":
            preco = 17
        elif tamanho == "G":
            preco = 21

    # Acumula o preço no total
    total += preco

    #opçao para continuar ou encerrar
    mais = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
    if mais == "S": # se escolhida continua...
       continue
    else:
       break  # Encerra o loop

# exibe total final
print(f"O valor total do seu pedido é: R$ {total:.2f}")
