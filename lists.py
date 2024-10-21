
#Añadir valores a una lista
names = ['christian', 'marc', 'carlos', 'pepe']

#Mostrar valores
print(f"Te presento a: {names[0].title()}.") 
print(f"Te presento a: {names[1].title()}.") 
print(f"Te presento a: {names[2].title()}.") 
print(f"Te presento a: {names[3].title()}.") 

#Modifica el valor en la posición 3
names[3] = "Pablo"
print(f"Ay, no, este último se llamaba: {names[3]}")

#Crea una lista vacía
apellidos = []

#Añade valores a la lista vacía de forma correlativa
apellidos.append("Morales")
apellidos.append("Rocher")
apellidos.append("Catalán")
apellidos.append("Rubio")

print(f"Su nombre completo es: {names[0].title()} {apellidos[0]}.") 
print(f"Su nombre completo es: {names[1].title()} {apellidos[1]}.") 
print(f"Su nombre completo es: {names[2].title()} {apellidos[2]}.") 
print(f"Su nombre completo es: {names[3].title()} {apellidos[3]}.") 

#Añadir un valor en la posición elegida, desplazando a los demás una posición
names.insert(1, "Iván")
apellidos.insert(1, "De la Fe")

print(f"Ahora en la posición 1 está: {names[1]} {apellidos[1]}")
print(f"Ahora en la posición 2 está: {names[2].capitalize()} {apellidos[2]}")


#Borramos a Iván de la Fe de la lista
del names[1]
del apellidos[1]
print(names)
print(apellidos)

#Borrar el último elemento de la lista, pero guardando la memoria
popped_name = names.pop()
popped_apellido = apellidos.pop()

print(f"El usuario eliminado es {popped_name} {popped_apellido}")


motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0) #Elimina el valor Honda y lo guarda en la variable first_owned
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles[0]) #al haber sido borrado honda, ahora yamaha pasa a tener la primera posición
