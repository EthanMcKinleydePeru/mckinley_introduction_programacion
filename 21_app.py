def calcularPrecio (monto, descuento):
    montoDescuento = monto*descuento
    return monto-montoDescuento

precioFinal = calcularPrecio(2500,.10)
print(f"The precio final despues del descuento es S/ {precioFinal:.2f}")