squares = []

for value in range(1, 11):
    square = value ** 2 #Para calcular el cuadrado. Si 'value' fuera 5 -> 5 x 5
    squares.append(square) #Añade el valor al final de la lista 'squares'

print(squares,"\n")


digits = [1, 1, 2, 2, 3]

#SUM para sumar todos los valores de la lista
suma = sum(digits)
print(f"La suma de los valores da: {suma}")

#MAX muestra el valor más alto de la lista
alto = max(digits)
print(f"El valor más bajo es: {alto}")

#MIN muestra el valor mmás bajo de la lista
bajo = min(digits)
print(f"El valor más bajo es: {bajo}")


