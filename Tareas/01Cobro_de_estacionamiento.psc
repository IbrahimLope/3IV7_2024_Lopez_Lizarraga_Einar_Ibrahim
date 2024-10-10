Algoritmo Cobro_de_estacionamiento
	
	Definir horaentrada, minutoentrada, horasalida, minutosalida Como real
	Definir totalhoras, totalminutos, minutostotales Como real
	Definir totalcobro Como real
	
	//Entrada de datos
	Escribir "Ingrese hora de entrada: (Formato 24h) "
	Leer horaentrada
	Escribir "Ingrese minuto de entrada: (Formato 0 - 59) "
	Leer minutoentrada
	
	Escribir "Ingrese hora de Salida: (Formato 24h) "
	Leer horasalida
	Escribir "Ingrese minuto de salida: (Formato 0 - 59) "
	Leer minutosalida
	
	//Proceso 
	//Calcular el tiempo total en minutos
	totalhoras = horasalida - horaentrada
	totalminutos = minutosalida - minutoentrada
	
	//evaluar casos
	Si totalminutos < 0 Entonces
		totalminutos =+ 60
		totalhoras =- 1
	Fin Si
	
	//Convertir a minutos
	totalminutos = (totalhoras*60) + totalminutos
	
	//Calcular cobro
	totalcobro = 0
	
	//hora completa
	Si totalminutos >= 60 Entonces
		totalcobro = totalcobro + (totalminutos/60)*15
	FinSi
	
	//fraccion de hora
	minutosrestantes = totalminutos%60
	Si minutosrestantes > 0 Entonces
		fraccionesde15 = minutosrestantes //Obtiene los 15min
		//Cobrar fraccion
		totalcobro = totalcobro + fraccionesde15 * 6
	FinSi
	
	//Mostrarlo
	Escribir "El total a pagar es de: ", totalcobro, " Pesos"
	
FinAlgoritmo
