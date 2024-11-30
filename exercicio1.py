#imprime mensagem  de boas vindas com nome da dona da loja
print("Bem vindo a loja da Yasmin Fioramonte")
print(" ")

#entradas com valor do pedido e quantidade de parcelas
valorDoPedido = float(input("Entre com o valor do pedido " ))
quantidadesDeParcelas = int(input("Entre com a quantidade de parcelas" + " "))

# condição referente ao parcelamento até 3x, nesta condição não temos acréscimo de juros.
if quantidadesDeParcelas < 4:
        taxaDeJuros = 0
        valorDaParcela = valorDoPedido * (1 + (taxaDeJuros / 100))  / quantidadesDeParcelas #calcula valor da parcela
        totalDoPedidoParcelado = valorDaParcela * quantidadesDeParcelas #calcula valor total parcelado
        print(f'Valor das parcelas é de: R$ {valorDaParcela}')
        print(f'Valor total parcelado é de: {totalDoPedidoParcelado}')

# aqui temos o parcelamento de 4 á 5x , com acréscimo de 4%
elif 4 <= quantidadesDeParcelas  < 6:
        taxaDeJuros = 4
        valorDaParcela = valorDoPedido * (1 + (taxaDeJuros / 100) ) / quantidadesDeParcelas  #calcula valor da parcela
        totalDoPedidoParcelado = valorDaParcela * quantidadesDeParcelas #calcula valor total parcelado
        print(f'Valor das parcelas é de: R${valorDaParcela}')
        print(f'Valor total parcelado é de: R${totalDoPedidoParcelado}')

# aqui temos o parcelamento de 6 á 8x, com juros de 8%
elif  6 <= quantidadesDeParcelas  < 9:
        taxaDeJuros = 8
        valorDaParcela = valorDoPedido * (1 + ( taxaDeJuros / 100) ) / quantidadesDeParcelas  #calcula valor da parcela
        totalDoPedidoParcelado = valorDaParcela * quantidadesDeParcelas #calcula valor total parcelado
        print(f'Valor das parcelas é de: R${valorDaParcela}')
        print(f'Valor total parcelado é de: R${totalDoPedidoParcelado}')

# parcelamentos de 9 á 12x, juros de 13%
elif  9 <= quantidadesDeParcelas  < 13:
        taxaDeJuros = 16
        valorDaParcela = valorDoPedido * (1 + (taxaDeJuros / 100) ) / quantidadesDeParcelas  #calcula valor da parcela
        totalDoPedidoParcelado = valorDaParcela * quantidadesDeParcelas #calcula valor total parcelado
        print(f'Valor das parcelas é de: R${valorDaParcela}')
        print(f'Valor total parcelado é de: R${totalDoPedidoParcelado}')

# parcelamentos apartir de 13% , com juros de 32%
else:
        quantidadesDeParcelas >= 13
        taxaDeJuros = 32
        valorDaParcela = valorDoPedido * (1 + (taxaDeJuros / 100) ) / quantidadesDeParcelas  #calcula valor da parcela
        totalDoPedidoParcelado = valorDaParcela * quantidadesDeParcelas #calcula valor total parcelado
        print(f'Valor das parcelas é de: R${valorDaParcela}')#imprime valor das parcelas com os juros , dependendo da opção de parcelamento escolhida pelo usuário
        print(f'Valor total parcelado é de: R${totalDoPedidoParcelado}')#imprime total final com juros

