# Preguntar para el monto que quiere cambiar

soles = float(input("Ingrese el monto en soles (PEN): "))
tasa = float(input("Ingrese la tasa de cambio actual (1USD = ? PEN): "))
# Cambiar los soles a los dolares

dolares = soles/tasa

# Imprimir los resultos

print("--- Conversion en Global Change ---")
print(f"Monto en soles: S/ {soles}")
print(f"Tasa de cambio: 1 USD = S/ {tasa}")
print(f"Equivalente en dolares: $ {dolares}")