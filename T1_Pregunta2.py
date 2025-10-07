#Preguntar por la edad del pasajero
edad = int(input("Ingrese la edad del pasajero: "))

#Usar if, elif, y else para imprimir cual tarifa el pasajero necesita pagar
if edad < 12:
    print("Tarifa infantil: S/ 3.00")
elif edad < 60:
    print("Tarifa regular: S/ 5.00")
else:
    print("Tarifa especial: S/ 2.00")