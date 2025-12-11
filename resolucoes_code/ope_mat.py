# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def calculadora_basica():
    """
    Solicita dois números ao usuário e realiza as quatro operações básicas.
    """
    print("## Operações Aritméticas Básicas ##")

    # 1. Recebendo os inputs
    try:
        # Usamos float() para permitir números decimais e inteiros
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        # Tratamento de erro caso o usuário digite algo que não é um número
        print("Erro: A entrada deve ser um número válido.")
        return # Encerra a função se a entrada for inválida

    print("\n--- Resultados ---")

    # 2. Realizando as Operações
    
    # Adição
    soma = num1 + num2
    print(f"➕ Adição: {num1} + {num2} = {soma}")

    # Subtração
    subtracao = num1 - num2
    print(f"➖ Subtração: {num1} - {num2} = {subtracao}")

    # Multiplicação
    multiplicacao = num1 * num2
    print(f"✖️ Multiplicação: {num1} * {num2} = {multiplicacao}")

    # Divisão
    if num2 != 0:
        # A divisão só é executada se o segundo número não for zero
        divisao = num1 / num2
        print(f"➗ Divisão: {num1} / {num2} = {divisao}")
    else:
        # Tratamento de erro para divisão por zero (um conceito fundamental!)
        print("➗ Divisão: Não é possível dividir por zero (resultado indefinido).")

# Chama a função para executar o programa
calculadora_basica()