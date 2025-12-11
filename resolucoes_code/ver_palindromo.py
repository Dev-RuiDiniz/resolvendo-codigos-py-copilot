def verificar_palindromo():
    """
    Solicita uma palavra ao usuário e verifica se ela é um palíndromo.
    """
    print("## Verificador de Palíndromos ##")
    
    # 1. Entrada e Preparação da String
    # .strip() remove espaços em branco no início/fim
    # .lower() converte tudo para minúsculas, garantindo que "Arara" == "arara"
    palavra_original = input("Digite uma palavra ou frase: ").strip().lower()
    
    # Remove espaços se for uma frase, para que "A mala" seja um palíndromo
    palavra_limpa = palavra_original.replace(" ", "")
    
    # 2. Inversão da String (O Truque de Python!)
    # Sintaxe de fatiamento: [start:stop:step]
    # [::-1] significa: Comece no início (vazio), vá até o fim (vazio), 
    # pulando de -1 em -1 (de trás para frente).
    palavra_invertida = palavra_limpa[::-1]
    
    # 3. Comparação e Resultado
    
    print("\n--- Análise ---")
    print(f"Palavra limpa (original): {palavra_limpa}")
    print(f"Palavra invertida: {palavra_invertida}")
    
    if palavra_limpa == palavra_invertida:
        print(f"\n🎉 A palavra/frase '{palavra_original}' É um PALÍNDROMO!")
    else:
        print(f"\n❌ A palavra/frase '{palavra_original}' NÃO é um palíndromo.")

verificar_palindromo()