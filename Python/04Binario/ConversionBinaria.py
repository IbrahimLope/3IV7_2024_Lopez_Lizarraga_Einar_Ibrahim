def Conversionbinaria():
    while True:
        num = int(input("Ingresa el número que se desea convertir: "))
        
        binario = ""

        if num >= 0:
            while num > 0:
                residuo = num % 2
                binario = str(residuo) + binario
                num = num // 2  # Utilizamos la división entera

            if binario == "":
                binario = "0"

            print("El número en binario es:", binario)
        else:
            print("Ingrese un número mayor o igual a 0")

Conversionbinaria()