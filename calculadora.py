# Cria variáveis e armazena os dados digitados pelo usuário
numeroUm = int(input('Digite o primeiro número: '))
numeroDois = int(input('Digite o segundo número: '))

# Cria variável e armazena a opção de operação a realizar
opEscolhida = int(input(f'\nQual operação deseja realizar?\n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\nOpção: '))

# Cria função para realizar o cálculo, que recebe os números digitados por parâmetro
def realizaCalculo(numUm, numDois):
    
    # Realiza match com a opção escolhida
    match(opEscolhida):
             
        # Caso opção tenha sido adição
        case 1:

            # Soma os números e retorna o resultado
            resultado = numUm + numDois
            return resultado
            
        # Caso opção tenha sido subtração
        case 2:

            # Subtrai os números e retorna o resultado
            resultado = numUm - numDois
            return resultado
            
        # Caso opção tenha sido multiplicação
        case 3:

            # Multiplica os números e retorna o resultado
            resultado = numUm * numDois
            return resultado
            
        # Caso opção tenha sido divisão
        case 4:

            # Divide os números e retorna o resultado
            resultado = numUm / numDois
            return resultado

# Mostra o resultado da operação na tela
print(f'Resultado: {realizaCalculo(numeroUm, numeroDois)}')