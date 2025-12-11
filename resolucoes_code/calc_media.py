def calcular_media_notas():
    """
    Solicita três notas ao usuário e calcula a média aritmética.
    """
    print("## Calculadora de Média de Três Notas ##")
    
    # Lista para armazenar as notas
    notas = []
    
    # 1. Entrada de Dados e Validação
    
    # Usamos um loop para solicitar as notas e garantir a validade
    for i in range(1, 4):
        while True:
            try:
                # O input é convertido para float para aceitar notas decimais
                nota = float(input(f"Digite a nota {i}/3: "))
                notas.append(nota)
                break  # Sai do loop interno se a nota for válida
            except ValueError:
                print("⚠️ Erro: Por favor, digite um valor numérico válido para a nota.")
    
    # 2. Cálculo da Média
    
    # A fórmula da média aritmética é: (Soma dos valores) / (Quantidade de valores)
    
    # 2a. Soma das notas
    soma_notas = notas[0] + notas[1] + notas[2] 
    # Ou, usando a função sum() do Python: soma_notas = sum(notas)
    
    # 2b. Quantidade de notas
    quantidade_notas = len(notas) # Usamos len(notas) para obter a contagem (que é 3)
    
    # 2c. Cálculo final (divisão)
    # É fundamental usar parênteses para garantir que a soma seja feita ANTES da divisão.
    media = soma_notas / quantidade_notas 

    # 3. Exibindo o Resultado
    print("\n--- Resultado do Cálculo ---")
    print(f"Notas fornecidas: {notas}")
    print(f"Soma das notas: {soma_notas}")
    print(f"Média Aritmética: {media:.2f}") # Exibe a média com 2 casas decimais

calcular_media_notas()