package main

import "fmt"

// comentario de línea
/*Comentario de líena multiple*/

func saludar(nombre string) string {
	mensaje := fmt.Sprintf("Hola, %v. Bienvenido!", nombre)

	return mensaje
}

func main() {
	fmt.Println("Hello GO!")
	fmt.Println(saludar("Franco"))
}

/*
En GO el operador ":=" es un atajo para declarar e inicializar una variable en una sola línea. El valor que se encuentra a la derecha, determina el tipo de dato de la variable.

%v se utiliza para sustituir el nombre del parámetro por el valor de dicho parámetro en la posición donde se encuentra %v. Por lo tanto, la salida de la función saludar será "Hola 'nombre'. Bienvenido!"


*/
