codigoEmpleado = int(input("Ingrese el codigo del empleado: "))
nombre = input("Ingrese el nombre del empleado: ")
horasMes = int(input("ingrese cantidad de horas trabajadas al mes"))
valorHora = int(input("Valor de hora trabajada: "))
porcentajeRetencion = input("Porcentaje de retencion en la fuente ")

salarioBruto = horasMes * valorHora
retencion = (float(porcentajeRetencion) / 100) * salarioBruto
salarioNeto = salarioBruto - retencion

