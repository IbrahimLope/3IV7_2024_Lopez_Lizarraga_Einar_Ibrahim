Algoritmo escribir_primeros_100_numeros
	
	// Escribe los primeros 100 números naturales
	Definir numerito Como Entero
	Definir K Como Entero
	
	numerito = 1
	K = 1
	Repetir
		Mientras K <= 100 Hacer
			Escribir numerito
			numerito = numerito + 1
			K = K + 1
		Fin Mientras
		Escribir " "
		Escribir " "
		Escribir "¿Desea ingresar otro número? (repetir (1)/salir(2):"
		Leer RP
	Hasta que RP <> '1'

FinAlgoritmo
