Algoritmo ReservasHotel
	
	Definir ocupada, disponibles, NHabitaciones, habitacionestotales Como Entero
	Definir Ocupacion Como Real
	
	
	habitacionestotales = 10
	NHabitaciones = 10
	ocupadas = 0
	disponibles = NHabitaciones
	
	
	Para i = 1 hasta 10 con paso 1 Hacer
		reservas = 0
	FinPara
	
	
	Mientras Opcion <> 5 Hacer
		Escribir "1. Registrar reserva"
		Escribir "2. Cancelar reserva"
		Escribir "3. Consultar disponibilidad"
		Escribir "4. Porcentaje de ocupacion"
		Escribir "4. Salir"
		Leer Opcion 
		
		Segun Opcion hacer
		Caso 1: 
			Si disponibles>0 Entonces
				Escribir "¿Que habitacion quieres reservar? (1-", NHabitaciones ")"
				Leer habitacion
				Escribir "Ingresa el dia de llegada en formato (dd/mm/aa)"
				Leer llegada
				Escribir "Ingresa el dia de salida en formato (dd/mm/aa)"
				leer salida
				ocupadas = ocupadas + 1
				disponibles = disponibles - 1
			SiNo 
				Escribir "No hay habitaciones disponibles"
			FinSi
				
		Caso 2:
			Si ocupada>0 Entonces
				Escribir "¿Que habitacion deseas cancelar?"
				Leer NHabitaciones
				Escribir "Ha sido cancelada"
				ocupada = ocupada - 1
				disponibles = disponibles + 1
			SiNo 
				Escribir "No hay registro de reservas"
			FinSi
			
		Caso 3:
			Escribir "El total de habitaciones disponibles es: ", disponibles
			
		Caso 4: 
			Ocp=(ocupada/habitacionestotales)*100
				Escribir "El porcentaje actual de ocupacion es: ", Ocp "%"
				
		FinSegun
		
	FinMientras
	
FinAlgoritmo
