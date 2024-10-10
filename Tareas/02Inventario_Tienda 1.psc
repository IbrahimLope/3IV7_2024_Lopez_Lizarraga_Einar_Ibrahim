Algoritmo Inventario_Tienda
	
	Definir producto como texto
	Definir codigoproducto, cantidad Como Entero
	Definir precio como real
	
	//Menu de seleccion
	Mientras Opcion <> 6 Hacer
		Escribir "1. Ingresa un nuevo producto"
		Escribir "2. Actualiza un producto"
		Escribir "3. Consulta el Inventario"
		Escribir "4. Registrar venta"
		Escribir "5. Generar reporte"
		Escribir "6. Salir"
		Leer Opcion 
		
		Segun Opcion  Hacer
			Caso 1:
				Escribir "Ingresa el nombre: "
				Leer producto
				Escribir "Ingresa el codigo del producto: "
				Leer codigoproducto
				Escribir "Ingresa la cantidad: "
				Leer cantidad
				Escribir "Ingresa el precio: "
				Leer precio
				SckTotal <- SckTotal + cantidad
				
			Caso 2:
				Escribir "Ingresa el codigo del producto a actualizar: "
				Leer codigoproducto
				Escribir "Ingresa nueva cantidad: "
				Leer cantidad
				SckTotal <- SckTotal + cantidad
				
			Caso 3:
				Escribir "Consultar inventario"
				Escribir "Nombre del producto: ", producto
				Escribir "Codigo del producto: ", codigoproducto
				Escribir "Precio del producto: ", precio
				
			Caso 4: 
				Escribir "Registra una venta"
				Escribir "Ingresa el codigo del producto: "
				Leer codigoproducto
				Escribir "Ingresa la cantidad de producto: "
				Leer cantidad
				Escribir "Venta registrada"
				totalVentas <- totalVentas + cantidad
				SckTotal <- SckTotal - cantidad
				
			Caso 5:
				Escribir "Reporte diario:"
				Escribir "Stock total: ", SckTotal
				Escribir "Total ventas: ", totalVentas 
				
		Fin Segun
	Fin Mientras
	
	
FinAlgoritmo
