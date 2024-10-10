Algoritmo ExamenAlgoritmia_Censo
    
	Escribir 'Ingresa la cantidad de personas: '
    Leer N
	
    Mientras N<1 Hacer
        Escribir 'La cantidad de personas debe ser positiva. Intenta nuevamente: '
        Leer N
    FinMientras
	
    Dimension nacimiento(N), fallecimiento(N)
	
    Para i<-1 Hasta N Con Paso 1 Hacer
        Escribir 'Ingresa el año de nacimiento ', i
        Leer nacimiento[i]
        Mientras nacimiento[i]<=0 O nacimiento[i]>2024 Hacer
            Escribir 'El año de nacimiento debe ser mayor a 0 y menor o igual a 2024. Intenta nuevamente: '
            Leer nacimiento[i]
        FinMientras
        
        Escribir 'Ingresa el año de fallecimiento ', i
        Leer fallecimiento[i]
        Mientras fallecimiento[i]<=0 O fallecimiento[i]>2024 O fallecimiento[i]<nacimiento[i] Hacer
            Escribir 'El año de fallecimiento debe ser mayor o igual al año de nacimiento y menor o igual a 2024. Intenta nuevamente: '
            Leer fallecimiento[i]
        FinMientras
    FinPara
	
    consulta <- 0
    
	Escribir 'Ingresa el año de consulta: '
    Leer consulta
    Mientras consulta<=0 O consulta>2024 Hacer
        Escribir 'El año de consulta debe ser mayor a 0 y menor o igual a 2024. Intenta nuevamente: '
        Leer consulta
    FinMientras
	
    convida <- 0
    masjoven <- 10000
    masanciano <- -1
	
    Para j<-1 Hasta N Con Paso 1 Hacer
        Si consulta >= nacimiento[j] Y consulta <= fallecimiento[j] Entonces
            convida <- convida + 1
            edad <- consulta - nacimiento[j]
            Si edad < masjoven Entonces
                masjoven <- edad
            FinSi
            Si edad > masanciano Entonces
                masanciano <- edad
            FinSi
        FinSi
    FinPara
	
    Si convida > 0 Entonces
        Escribir 'Año: ', consulta
        Escribir 'El más joven: ', masjoven
        Escribir 'El más anciano: ', masanciano
        Escribir 'Personas vivas: ', convida
    FinSi
	
FinAlgoritmo
