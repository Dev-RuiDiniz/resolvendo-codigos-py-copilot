# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

# 1. Recebendo os dados do usuário
# A função input() sempre retorna uma string, o que é perfeito para concatenação.
dado1 = input("Por favor, digite o primeiro dado (ex: nome): ")
dado2 = input("Agora, digite o segundo dado (ex: sobrenome): ")

# 2. Concatenação usando f-string (Melhor Prática)
# As f-strings permitem embutir expressões e variáveis dentro da string 
# de forma concisa e legível. O 'f' antes das aspas indica que é uma f-string.
string_concatenada_fstring = f"Dados Combinados: {dado1} {dado2}"

# 3. Concatenação usando o operador '+' (Método Clássico)
# Este método funciona, mas pode ser menos eficiente para muitas concatenações.
string_concatenada_operador = "Dados Combinados: " + dado1 + " " + dado2

# 4. Exibindo os resultados
print("\n--- Resultados ---")
print(f"Versão f-string: {string_concatenada_fstring}")
print(f"Versão operador +: {string_concatenada_operador}")