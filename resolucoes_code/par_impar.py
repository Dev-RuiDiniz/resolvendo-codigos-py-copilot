def verificar_par_impar_otimizado():
    """
    Recebe um número inteiro e verifica par/ímpar usando uma expressão 
    condicional (operador ternário) para maior concisão.
    """
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")
        return

    # Otimização: Operador Ternário
    # Estrutura: [valor_se_verdadeiro] if [condicao] else [valor_se_falso]
    resultado = "PAR" if (numero % 2) == 0 else "ÍMPAR"

    print(f"O número {numero} é {resultado}.")

verificar_par_impar_otimizado()