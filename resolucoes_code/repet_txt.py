def repetir_texto():
    """
    Solicita uma string e um número inteiro, e repete a string
    o número de vezes informado.
    """
    print("## Repetidor de Texto Python ##")
    
    # 1. Entrada da String
    texto = input("Digite o texto que deseja repetir: ")
    
    # 2. Entrada do Número de Repetições (com tratamento de erro)
    try:
        # Garante que a entrada para repetições seja um número inteiro positivo
        repeticoes = int(input("Quantas vezes você deseja repetir o texto (número inteiro)? "))
        
        if repeticoes < 0:
            print("Erro: O número de repetições deve ser positivo.")
            return

    except ValueError:
        print("Erro: A entrada de repetições deve ser um número inteiro válido.")
        return

    # 3. Executando a Repetição
    # Python permite a multiplicação de uma string por um inteiro:
    # "a" * 3 resulta em "aaa"
    texto_repetido = texto * repeticoes

    # 4. Exibindo o Resultado
    print("\n--- Resultado ---")
    print(f"Texto original: '{texto}'")
    print(f"Número de repetições: {repeticoes}")
    print(f"Resultado final:\n{texto_repetido}")

repetir_texto()