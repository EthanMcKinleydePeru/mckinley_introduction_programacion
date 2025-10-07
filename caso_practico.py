nombre = str(input("Nombre del vendedor: "))
sueldo_base = float(input("Sueldo Base (S/): "))
ventas = float(input("Ventas del Mes (S/): "))

comision = ventas * .08

if(ventas >= 8000):
    bono = 300
else:
    bono = 0

total_por_impuestos = bono + comision

impuestos_a_la_renta = total_por_impuestos * .08

sueldo_final = sueldo_base + comision + bono - impuestos_a_la_renta

print(f"--- Reporte para {nombre} ---")
print(f"Sueldo Base      : S/ {sueldo_base}")
print(f"Ventas del Mes   : S/ {ventas}")
print("--------------------------------")
print(f"+ Comision  (8%)   : S/ {comision}")
print(f"+ Bono             : S/ {bono}")
print(f"- Impuesto  (8%)   : S/ {impuestos_a_la_renta}")
print("--------------------------------")
print(f"Sueldo Final Neto  : S/ {sueldo_final}")
print("================================")