list_cars = ['toyota', 'citroën', 'audi', 'tesla']

list_cars.sort() #Ordena el listado de coches de la A a la Z
print(list_cars)

list_cars.sort(reverse=True) #Ordena el listado de la Z a la A
print (list_cars)

print(sorted(list_cars)) # sorted() mostrará la lista ordenada (A a Z) termporalmente sin alterar la lista
print(sorted(list_cars, reverse=True)) #Lo mismo pero de la Z a la A

#reverse() da la vuelta al orden de los elementos 
list_cars.reverse()
print(list_cars)

#Para saber el número de elementos que contiene la lista
num_cars = len(list_cars)
print(f"Hay {num_cars} coches")