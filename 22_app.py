def obtener_datos_empleado():
   nombre = input("Ingresa el nombre del colaborador");
   salarioBruto = input(f"Ingresa el salario bruto de {nombre} en S/.");
   porcentajeDescuento = input("Ingresa el porcentaje de descuento en %");

   salarioBrutoValor = float(salarioBruto)
   porcentajeDescuentoValor = float(porcentajeDescuento)

   return nombre, salarioBrutoValor, porcentajeDescuentoValor


