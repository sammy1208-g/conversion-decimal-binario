#Codigo para convertir un numero decimal (de 2 cifras) a binario de 8 bits

decimal = int(input("Ingresa un número decimal: "))
binario = decimal_a_binario(decimal)
def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el numero (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario

print(f"El numero {decimal} es {binario} en binario")