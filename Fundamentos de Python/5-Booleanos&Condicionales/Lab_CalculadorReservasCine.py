#En este taller, practicarás cómo usar booleanos y declaraciones condicionales en Python construyendo un calculador de reservas de entradas de cine.

#Paso1  -  variables que almacenan información sobre el usuario y la función de la película.
base_price =  15
age = 21

#Paso2  - almacenar algunos valores de cadena sobre el boleto de la película.
seat_type =  'Gold'
show_time = 'Evening'

#Paso3 -   verificarás si el usuario es elegible para reservar un boleto de cine según su edad.

if age > 17:
    print('User is eligible to book a ticket')

#Paso 4 - verificarás si el usuario tiene permitido reservar un espectáculo nocturno según su edad.
#Paso5 -  agrega una cláusula else a tu declaración if
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

#Paso6 -  Algunas informaciones solo pueden ser verdaderas o falsas. Como has aprendido en lecciones anteriores, esto puede representarse usando valores booleanos.

#is_member = True
is_weekend = False

#Paso7 El usuario califica para un descuento de membresía si es miembro.
discount =  0

#Paso8 - Crea una sentencia if para verificar si is_member es verdadero.
#Paso9 - manejar el caso cuando el usuario no califique para un descuento de membresía.
if is_member:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print(f'Discount: {discount}')

#Paso10 -  el operador and se usa para verificar si múltiples condiciones son verdaderas. 
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print(f'Discount: {discount}')

#Paso 11 - Ahora cambia el valor de la variable is_member a False ya que el usuario no es miembro. Después de eso, verás que el valor de discount ahora permanece en 0, porque ambas condiciones deben cumplirse para que se aplique el descuento.

is_member = False

#Paso12  - Ahora crea una variable llamada extra_charges y asígnale el valor 0. Esto representará los cargos extra que se aplicarán al boleto de cine para las funciones nocturnas. El operador de igualdad (==) verifica si dos valores son iguales y evalúa a True o False.
#Paso13 -   agrega una cláusula else a tu sentencia if e imprime No extra charges will be applied dentro del cuerpo de else. Esto imprimirá el mensaje solo cuando la condición de cargos extra sea falsa.
#Paso 14 -  Actualiza la condición de la línea if show_time == 'Evening': usando el operador or para combinar la condición existente con una segunda condición que verifique si is_weekend es verdadera.

extra_charges = 0
if show_time == 'Evening' or is_weekend:
    extra_charges = 2
    print('Extra charges will be applied')   
else:
    print('No extra charges will be applied')
print(f'Extra charges: {extra_charges}')

#Paso 15 -  Ahora verificarás si el usuario cumple con las condiciones para reservar un boleto de cine. Los usuarios con edad 21 o más siempre pueden reservar boletos sin ninguna restricción.
if age >= 21:
    print('Ticket booking condition satisfied')
else:
    print('Ticket booking failed due to restrictions')


#Paso16 - Los usuarios que tengan al menos 18 años pero menos de 21 pueden reservar entradas, pero solo cuando el show_time no sea Evening.

if age >=21 or age>=18 and show_time != 'Evening':
   print('Ticket booking condition satisfied')
else:
    print('Ticket booking failed due to restrictions')

#Paso 17 -  Los usuarios que tengan al menos 18 años pero menos de 21 pueden reservar funciones nocturnas si son miembros. agregar otra condición usando el operador or para verificar si is_member es verdadero. Usa paréntesis () para agrupar las condiciones show_time != 'Evening' e is_member


if age >=21 or age>=18 and (show_time != 'Evening' or is_member):
   print('Ticket booking condition satisfied')
else:
    print('Ticket booking failed due to restrictions')


#Paso18 - Ahora calcularás los cargos por servicio según el tipo de asiento que el usuario haya seleccionado.
# una sentencia if también puede colocarse dentro del cuerpo de otra sentencia if. Esto se llama una sentencia if anidada.


if age >=21 or age>=18 and (show_time != 'Evening' or is_member):
   print('Ticket booking condition satisfied')
   service_charges = 0
   if seat_type == 'Premium':
       service_charges = 5
else:
    print('Ticket booking failed due to restrictions')


#Paso19 - dentro del cuerpo de la declaración externa if, agrega una cláusula else a la declaración anidada
if age >=21 or age>=18 and (show_time != 'Evening' or is_member):
   print('Ticket booking condition satisfied')
   service_charges = 0
   if seat_type == 'Premium':
       service_charges = 5
   else: 
        service_charges  = 1
else:
    print('Ticket booking failed due to restrictions')

#Paso20 - La sentencia if...elif...else se usa para verificar múltiples condiciones en orden.

if age >=21 or age>=18 and (show_time != 'Evening' or is_member):
   print('Ticket booking condition satisfied')
   service_charges = 0
   if seat_type == 'Premium':
       service_charges = 5
   elif seat_type == ('Gold'):
        service_charges = 3
   else: 
        service_charges  = 1
   print(f'Service charges: {service_charges:.2f}')
else:
    print('Ticket booking failed due to restrictions')


#Paso21 -   calcularás el precio final del boleto de cine usando los valores calculados en los pasos anteriores. El precio final del boleto se calcula sumando los cargos adicionales y los cargos por servicio al precio base, y luego restando el descuento.

if age >=21 or age>=18 and (show_time != 'Evening' or is_member):
   print('Ticket booking condition satisfied')
   service_charges = 0
   if seat_type == 'Premium':
       service_charges = 5
   elif seat_type == ('Gold'):
        service_charges = 3
   else: 
        service_charges  = 1
   print(f'Service charges: {service_charges:.2f}')

   final_price = base_price + extra_charges + service_charges - discount
   print(f'Final price of ticket:{final_price:.2f}')
else:
    print('Ticket booking failed due to restrictions')