Algoritmo ParImparConREPETIR
	
    Definir numerito Como Entero
    Definir continuar Como Caracter
	
    Repetir
        Escribir "Ingrese un n�mero:"
        Leer numerito
		
        Si numerito % 2 = 0 Entonces
            Escribir "El n�mero ", numerito, " es par."
        Sino
            Escribir "El n�mero ", numerito, " es impar."
        FinSi
		Escribir " "
		Escribir " "
        Escribir "�Desea ingresar otro n�mero? (repetir (1)/salir(2):"
        Leer RP
    Hasta que RP <> '1'
	
FinAlgoritmo
