#Datos de entrada
sueldo = float (input("Sueldo: "))
situacion = input("Situación (1/2/3): ")
num_hijos = int(input("Número de hijos: "))

#Calcular exención
exencion = 0
if situacion == '1':
    if num_hijos <= 0:
        exencion = 0
    elif num_hijos == 1:
        exencion = 15947
    else:
        exencion = 17100

if situacion == '2':
    if num_hijos <= 0:
        exencion = 15546
    elif num_hijos == 1:
        exencion = 16481
    else:
        exencion = 17634
        
if situacion == '3':
    if num_hijos <= 0:
        exencion = 14000
    elif num_hijos == 1:
        exencion = 14516
    else:
        exencion = 15063
        
sueldo_a_retener = sueldo - exencion

#Retencion
if sueldo_a_retener <= 12450:
    porcentaje = 19
elif sueldo_a_retener <= 20200:
    porcentaje = 24
elif sueldo_a_retener <= 35200:
    porcentaje = 30
elif sueldo_a_retener <= 60000:
    porcentaje = 37
elif sueldo_a_retener <= 300000:
    porcentaje = 45
else:
    porcentaje = 47
    
monto_anual = sueldo_a_retener * porcentaje / 100
monto_mensual = monto_anual / 12

#Resultados
print("Sueldo anual: \t", sueldo)
print("Situacion:\t", situacion)
print("Base a retener:", sueldo_a_retener)
print("Porcentaje:\t", porcentaje, "%")
print("Total anual:\t", monto_anual)
print()
print("Retención mensual:", monto_mensual)