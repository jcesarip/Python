#LABORATORIO CONSTRUIR UN DIVISOR DE CUENTAS.
# Esta herramienta calculará cuánto debe cada persona después de sumar los costos de la comida y la propina.

#Paso1 Definir variable 
running_total= 0

#Paso2 número de personas que comparten la cuenta.
num_of_friend = 4

#Paso3 Cada curso tiene un costo. Como estos montos incluyen centavos, usarás el tipo float.
appetizers = 37.89
main_courses = 57.34
desserts =  39.39
drinks = 64.21

#Paso 4 Usa el operador += una vez para agregar appetizers, main_courses, desserts y drinks a running_total.

running_total  += appetizers  + main_courses + desserts + drinks
print(f'Total bill so far: {running_total}') #Total bill so far: 198.8299999999998

#Paso5 el grupo decide dejar una propina del 25%. Para calcular un porcentaje en Python, puedes multiplicar el total por el equivalente decimal del porcentaje.

tip = running_total * 0.25
print(f'Tip amount: {tip}') #Tip amount: 49.7074999999996

#Paso6 necesitas añadirla a tu running_total para encontrar el monto final de la cuenta. Usa el operador += para sumar el valor de tip a tu running_totalnecesitas añadirla a tu running_total para encontrar el monto final de la cuenta. Usa el operador += para sumar el valor de tip a tu running_total

running_total += tip
print(f'Total with tip: {running_total}') #Total  with tip: 248.537499999997

#Paso7  determinar cuánto debe cada persona dividiendo la cuenta total entre el número de amigos.
final_bill = running_total / num_of_friend
print(f'Bill per person: {final_bill}') #Bill per person: 62.1343749999999

#Paso8 redondear el resultado final.
each_pays =  round(final_bill,2)
print(f'Each person pays: {each_pays}') #Each person pays: 62.13







