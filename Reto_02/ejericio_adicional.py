"""DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos."""

def multiplos(multiplo3, multiplo5):
    count = 0
    for i in range(1,20):
        if (i%3 == 0 and i%5==0):
            print(multiplo3 + " " + multiplo5)
        elif (i%5 == 0):
            print(multiplo5)
        elif (i%3 == 0):
            print(multiplo3)
        else:
            print(i)
            count+=1
    return count

print("valor count:", multiplos("multiplo de 3", "multiplo de 5"))