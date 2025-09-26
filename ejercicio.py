

nombre_de_equipo = "Pantalla"
cuesta_de_equipo = 1000
cantidad = 5
igv = 18

monto_de_equipo = cuesta_de_equipo * cantidad
monto_IGV =  monto_de_equipo * (igv/100)
monto_a_pagar = monto_de_equipo + monto_IGV

print(monto_a_pagar)

print(f"El precio para comprar {cantidad} de tu Equipo: {nombre_de_equipo} con IGV de {igv}% es {monto_a_pagar}")