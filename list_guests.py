#3-4. Guest List
guest_list = ['Manolo', 'Paquito', 'Torrente', 'El Fary']

print(f"{guest_list[0]}, you are invited to my party")
print(f"{guest_list[1]}, you are invited to my party")
print(f"{guest_list[2]}, you are invited to my party")
print(f"{guest_list[3]}, you are invited to my party")



#3-5. Changing Guest List
print(f"Oh, finally {guest_list[1]} cannot come")

guest_list[1] ="Juanito"

print(f"A cambio vendrá {guest_list[1]}")

print(f"{guest_list[0]}, you are invited to my party")
print(f"{guest_list[1]}, you are invited to my party")
print(f"{guest_list[2]}, you are invited to my party")
print(f"{guest_list[3]}, you are invited to my party")



#3-6. More Guests
print(f"We've found a bigger table!")
guest_list.insert(0, "Francisco") #Añado a Francisco en la primera posición desplazando a los demás 1 pos. 
guest_list.insert(2, "Chucky de Cieza") #Añado al Chucky en medio de la lista
guest_list.append("Carmen de Mairena") #Añado a Carmen al final de la lista
print("-------------------")
#Invito a todos los invitados de la nueva lista
print(f"{guest_list[0]}, you are invited to my party")
print(f"{guest_list[1]}, you are invited to my party")
print(f"{guest_list[2]}, you are invited to my party")
print(f"{guest_list[3]}, you are invited to my party")
print(f"{guest_list[4]}, you are invited to my party")
print(f"{guest_list[5]}, you are invited to my party")
print(f"{guest_list[6]}, you are invited to my party")

#3-7. Shrinking Guest List
print("Finally the new bigger table is not arriving on time!")

print(guest_list)

#Borro desde atrás 5 elementos de la lista
popped_item = guest_list.pop() 
print(f"Sorry, {popped_item}, you cannot take part in the party anymore.")

popped_item = guest_list.pop() 
print(f"Sorry, {popped_item}, you cannot take part in the party anymore.")

popped_item = guest_list.pop() 
print(f"Sorry, {popped_item}, you cannot take part in the party anymore.")

popped_item = guest_list.pop() 
print(f"Sorry, {popped_item}, you cannot take part in the party anymore.")

popped_item = guest_list.pop() 
print(f"Sorry, {popped_item}, you cannot take part in the party anymore.")

#Recuerdo a los únicos dos invitados que están invitados a la fiesta
print(f"Hello, {guest_list[0]}, you are still in!")
print(f"Hello, {guest_list[1]}, you are still in!")

#Borro los dos últimos y muestro la lista vacía por pantalla
del guest_list[0]
del guest_list[1]


