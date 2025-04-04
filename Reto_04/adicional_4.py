""" * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas"""

# "cadena" != "anedac" - no es palindromo
# "oso" = "oso" - es palindromo


def esPalindromo(word1):
    if (word1.lower() == word1[::-1].lower()):
        return True
    else:
        return False

s = "Oso"
print(esPalindromo(s))

 