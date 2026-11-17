#Aplicar Metodos de uso de cadenas.
#Paso1 -  Declarar Variable.

email = 'alice.johnson@company.com'

#Paso2 - Usar funcion F-STRING
print(f'Email: {email}')#Email: alice.johnson@company.com

#Paso3  -  encontrar la posición de un carácter específico dentro de una cadena método integrado .find() 
at_position = email.find('@')
print(f'Position of @: {at_position}') #Position of @: 13

 #Paso4 extraer el nombre de usuario, que está antes del signo @
username = email[:at_position]
print(f'Username: {username}') #'Username: alice.johnson

#Paso5 verificar si una subcadena existe dentro de una cadena usando la palabra clave in. Devuelve True si la subcadena existe y False si no.

has_at =  ('@' in email)
print(f'Has @ symbol: {has_at}') #Has @ Symbol: True

#Paso6 - Verificar  otra cadena
has_com = ('.com' in email)
print(f'Has .com: {has_com}')  # Has .com: true

#Paso7 -Los datos del mundo real suelen estar desordenados, con espacios extra y mayúsculas y minúsculas inconsistentes.
messy_name = '  sARaH dAVis  '
print(f"'Original name: {messy_name}'")

#Paso9  - El método .title() pone en mayúscula la primera letra de cada palabra. El método .strip() elimina los espacios en blanco de ambos extremos de una cadena.
clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")


#Paso 10 El método .lower() convierte todos los caracteres de una cadena a minúsculas.
messy_email = '  SARAH.DAVIS@COMPANY.COM  '
clean_email = messy_email.strip().lower()
print(f"Original email: '{messy_email}'")
print(f"Cleaned email: '{clean_email}'")

#Paso11 El método .upper() convierte todos los caracteres a mayúsculas. Esto es útil para placas de identificación o títulos
name_badge = clean_name.upper()
print(f'Name badge: {name_badge}')


#Paso12 Encuentra la posición del carácter @ en clean_email y guárdala en at_pos. Luego usa slicing para extraer todo lo que está antes de @ y guárdalo en email_user.

at_pos = clean_email.find('@')
email_user = clean_email[:at_pos]
print(f'Email: {clean_email}')
print(f'Username: {email_user}')

#Paso13 El método .replace(old, new) reemplaza cada ocurrencia de la subcadena old por otra, new. También puedes encadenarlo con otros métodos.

display_name  = email_user.replace('.',' ').title()
print(f'Display name: {display_name}')

#Paso14 .replace() para eliminar caracteres no deseados.
phone = '123-456-7890'
phone_clean = phone.replace('-','')
print(f'Phone with dashes: {phone}')
print(f'Phone without dashes: {phone_clean}')

#Paso14 El método .split(separator) divide una cadena en una lista de subcadenas en cada aparición de separator. 

full_address = '123 Main Street, Springfield, IL'
address_parts = full_address.split(', ')
print(f'Address parts: {address_parts}') #Address parts: ['123 Main Street', 'Springfield', 'IL']

#Paso15 El método .join(list) es el opuesto de .split(). Une una lista de cadenas en una sola cadena usando un separador.
rejoined = ' | '.join(address_parts)
print(f'Rejoined: {rejoined}')

#Paso16 comprobar cómo empieza una cadena. Python proporciona un método .startswith() para esto. Devuelve True si la cadena comienza con un prefijo dado; de lo contrario, devuelve False.comprobar cómo empieza una cadena. Python proporciona un método .startswith() para esto. Devuelve True si la cadena comienza con un prefijo dado; de lo contrario, devuelve False.

employee_code  = 'EMP-2024-SD'
starts_with_emp = employee_code.startswith('EMP')
print(starts_with_emp) #true

#Paso17 verificar cómo termina una cadena. Python proporciona el método .endswith() para esto. Devuelve True si la cadena termina con el sufijo dado y False si la cadena no termina con ese sufijo.
ends_with_com = clean_email.endswith('.com')
print(ends_with_com)#true


print(f'Code: {employee_code}')#Code: EMP-2024-SD
print(f'Starts with EMP: {starts_with_emp}')#Starts with EMP: True
print(f'Clean email: {clean_email}')#Clean email: sarah.davis@company.com
print(f'Ends with .com: {ends_with_com}')#Ends with .com: True

#Paso18  El método .count(substring) devuelve el número de ocurrencias no superpuestas de una subcadena en una cadena. 
dont_count = clean_email.count('.')
dash_count = employee_code.count('-')
print(f'Dots in email: {dont_count}')#Dots in email: 2
print(f'Dashes in code: {dash_count}')#Dashes in code: 2