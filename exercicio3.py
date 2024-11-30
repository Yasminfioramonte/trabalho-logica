print("Bem vindos à Fábrica de Camisetas da Yasmin Fioramonte")
print(" ")

print("Digite o modelo desejado:")
print("MCS- Manga Curta Simples")
print("MLS- Manga Longa Simples")
print("MCE- Manga Curta Estampada")
print('MLE- Manga Longa Estampada')

#Escolhe o modelo da camiseta
def escolha_modelo():
    while True:
        modelo = input("").upper()
        if modelo == "MCS":
            return 1.80
        elif modelo == "MLS":
            return 2.10
        elif modelo == "MCE":
            return 2.90
        elif modelo == "MLE":
            return 3.20
        else:
            print("Escolha inválida, entre com o modelo novamente.")
        
# Determina o número de camisetas e aplica desconto
def numero_camisetas():
    while True:
        try:
            numero = int(input("Digite o número de camisetas: "))
            if numero < 20:
               return numero# sem desconto 
            elif 20 <= numero < 200:
               return numero - (numero * 5/100) # Desconto de 5%  
            elif 200 <=  numero < 2000:
               return numero - (numero * 7/100)  # Desconto de 7% 
            elif 2000 <= numero <=20000:         
               return numero - ( numero * 12 / 100) #Desconto de 12%
            elif numero > 20000:
                print("Não aceitamos pedidos nesta quantidade.")
        except ValueError:
            print("Por favor, entre com o numero de camisetas novamente.")

# Escolhe o frete
def frete():
    print('Digite a opção de frete:')
    print('0- Retirar pedido na Fabrica')
    print('1-Frete por trasportadora')
    print('2-frete por sedex')
  
    while True:
        try:
            opcao_frete = int(input(""))
            if opcao_frete == 0:
                return 0
            elif opcao_frete == 1:
                return 100
            elif opcao_frete == 2:
                return 200
            else:
                print("Opção de frete inválida. Escolha 0, 1 ou 2.")
        except ValueError:
            print("Por favor, digite um valor valido.")

# Código principal
modelo_preco = escolha_modelo()
num_total = numero_camisetas()
frete_valor = frete()
    
total_pagar = (modelo_preco * num_total) + frete_valor

   
print(f"O valor total a pagar é: R${total_pagar:} ( Modelo : {modelo_preco} * Quantidade( Com Desconto):{num_total} + Frete : {frete_valor}. ")
    