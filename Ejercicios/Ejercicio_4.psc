Algoritmo Ejercicio_4
	
	// Realiza la sumatoria de los números enteros entre 1 y 10
	Definir suma Como Entero
	Definir numerito Como Entero
	
	suma = 0
	
Repetir	
	Para numerito = 1 Hasta 10 Hacer
		suma = suma + numerito
	Fin Para
	
	Escribir " "
	Escribir " "
	Escribir "La suma de los números del 1 al 10 es:", suma
	Escribir " "
	Escribir " "
	Escribir "¿Desea ingresar otro número? (repetir (1)/salir(2):"
	Leer RP
Hasta que RP <> '1'

FinAlgoritmo

