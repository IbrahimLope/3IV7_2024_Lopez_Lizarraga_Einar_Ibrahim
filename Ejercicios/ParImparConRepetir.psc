Algoritmo ParImparConREPETIR
	
    Definir numerito Como Entero
    Definir continuar Como Caracter
	
    Repetir
        Escribir "Ingrese un número:"
        Leer numerito
		
        Si numerito % 2 = 0 Entonces
            Escribir "El número ", numerito, " es par."
        Sino
            Escribir "El número ", numerito, " es impar."
        FinSi
		Escribir " "
		Escribir " "
        Escribir "¿Desea ingresar otro número? (repetir (1)/salir(2):"
        Leer RP
    Hasta que RP <> '1'
	
FinAlgoritmo
