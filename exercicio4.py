
print('Bem vindo a empresa da Yasmin Fioramonte.')#imprime nome 


lista_funcionarios = []  # Lista para armazenar dicionários de funcionários
id_global = 4914649  # Variável id_global.

def cadastrar_funcionario(id):#Função para cadastrar funcionários
    print('------------------------------------------------')#meu da função 
    print('-----------Menu Cadastrar funcionário----------')
    print(f'Id do funcionário: {id_global}')
    nome = input('Digite o nome do funcionário: ')
    setor = input('Digite o setor: ')
    salario = float(input("Digite o sálario: "))

    funcionario = { 'id': id_global,'nome': nome,'setor': setor,'salario': salario }#armazena informaçoe do funcionario cadastrado

    lista_funcionarios.append(funcionario.copy())  # Armazena uma cópia do dicionário na lista
   
def consultar_funcionarios():#função para consultar funcionário
   print('------------------------------------------------')
   print('-----------Menu Consultar funcionário----------')
   print('1- Consultar Todos')
   print("2- Consultar por Id")
   print("3- Consultar por Setor")
   print("4- Retornar ao menu")
   while True:#laço para validar opção escolhida
       opcao = int(input("Escolha a opção desejada: "))
       if (opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4):
        print('Opção inválida, digite novamente.')
        continue
       if opcao == 1:#Se opção 1 escolhida, consulta todos os funcionários
          for funcionario in lista_funcionarios:#procura o funcionario na lista 
              print(f"ID: {funcionario['id']}")
              print(f"Nome: {funcionario['nome']}")
              print(f"Setor: {funcionario['setor']}")
              print(f"Salário: R${funcionario['salario']:.2f}")
              print("------------------------")

        
       elif opcao == 2:#Se opção 2 escolhida, consulta por id
         consulta_id = int(input("Digite ID do funcionário: "))
         for funcionario in lista_funcionarios:#procura funcionario na lista 
           if funcionario['id'] == consulta_id:#consulta e compara id digitado com id existente na lista
              print(f"ID: {funcionario['id']}")#imprime id do funcionario
              print(f"Nome: {funcionario['nome']}")#imprime nome do funcionario
              print(f"Setor: {funcionario['setor']}")#imprime setor do funcionario
              print(f"Salário: R${funcionario['salario']:.2f}")#imprime salario do funcionario
              print("-----------------------------")
              break
           
       elif opcao == 3:#Se opção 3 enncontrada, consulta por setor
          consultar_setor = input("Digite o setor: ")
          for funcionario in lista_funcionarios:#procura funcionario na lista
           
             if funcionario['setor'].upper() == consultar_setor.upper():#consulta e compara setor digitado com setor existente na lista
                 print(f"ID: {funcionario['id']}")
                 print(f"Nome: {funcionario['nome']}")
                 print(f"Setor: {funcionario['setor']}")
                 print(f"Salário: R${funcionario['salario']:.2f}")
                 print("-----------------------------")
                 
       elif opcao == 4:#Se opção 4 escolhida, retorna ao menu principal
          return  
            

def remover_funcionario():
  while True:
      remover_id = int(input("Digite o ID do funcionário que deseja remover: "))#pede para que se digite o id que deseja remover
      for funcionario in lista_funcionarios:
          if funcionario['id'] == remover_id:
              lista_funcionarios.remove(funcionario)
              print(f" ID {remover_id} removido.")
              return
          else:
             print("Id inválido. Tente novamente.")

#código Pricipal
while True:# laço para validar escolha do menu
   print('----------------------------------------')
   print('-------------MENU Principal-------------')
   print('Escolha a opção desejada:')#opções do menu
   print("1. Cadastrar Funcionário")
   print("2. Consultar Funcionário")
   print("3. Remover Funcionário")
   print("4. Encerrar Programa")

   opcao = int(input(''))#deve escolher uma das opçoes do menu e digitar

   if (opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4):#caso usuário digite algo diferente dos numeros contidos no menu
        print('Opção inválida, digite novamente.')
        continue
   elif opcao == 1:#se opção 1 escolhida 
        id_global +=1# incrementa +1 ao id_global
        cadastrar_funcionario(id_global )#chama função cadastrar com id_global de incremento
        continue
   elif opcao == 2:#se opção 2 escolhida
        consultar_funcionarios() #chama função para consultar funcionário
        continue
   elif opcao == 3:#se  selecionada 
        remover_funcionario()#chama função de remover funcionario
        continue
   elif opcao == 4:# se selecionada , encerra programa.
     print("Programa encerrado.")
   break




