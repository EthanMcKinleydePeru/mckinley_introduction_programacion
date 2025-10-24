def obtener_datos_empleado():
   nombre = input("Ingresa el nombre del colaborador");
   salarioBruto = input(f"Ingresa el salario bruto de {nombre} en S/.");
   porcentajeDescuento = input("Ingresa el porcentaje de descuento en %");

   salarioBrutoValor = float(salarioBruto)
   porcentajeDescuentoValor = float(porcentajeDescuento)

   return nombre, salarioBrutoValor, porcentajeDescuentoValor

def imprimirBoleta(nombreEmpleado, salarioBrutoEmpleado, porcentajeDescuentoEmpleado):
    montoDescuento = salarioBrutoEmpleado*porcentajeDescuentoEmpleado
    salarioLiquido = salarioBrutoEmpleado-montoDescuento
    print(nombre)
    print(salarioBrutoEmpleado)
    print(montoDescuento)
    print(salarioLiquido)

imprimirBoleta(obtener_datos_empleado())
