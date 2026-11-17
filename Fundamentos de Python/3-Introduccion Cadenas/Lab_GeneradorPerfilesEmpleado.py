#Paso1  - Definir variables de texto.
first_name = "John"
last_name = "Doe"

print(first_name, last_name); #John Doe

#Paso2 - Concatenar Cadenas
full_name = first_name + last_name
print(full_name) #JhonDoe


#Paso3 - Concatenar Cadenas y agregar espacios
full_name1 = first_name + " " + last_name
print(full_name1) #Jhon Doe

#Paso4 Agregar direccion empleado en cadena
address = "123 Main Street"
print(address) #123 Main Street

#Paso5 - Agregar contendio a  la variable
address += ", Apartment 4B"
print(address) #123 Main Street, Apartment 4B

#Paso6 -  Variable Edad
employee_age = 28

#Paso7 -  Concatenar Cadena y numeros "Recuerda que Python no permite concatenar textos con numero direcatemente"
employee_info = full_name1 + ' is ' + str(employee_age) + ' years old'
print(employee_info) #Jhon Doe is 28 years old

#Paso 8 seguir usando str()
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info) # Experience: 5 years

#Paso9 - Optimizar concatenacion de cadenas usando f-strings
employee_card = f'Employee: {full_name} | Age: {employee_age}'

#Paso10 -  Agregar detalles a la tarjeta empleado.
position =  'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card) #Employee: Jhon Doe | Age: 28 | Position: Data Analyst | Salary: $75000

#Paso11 - Extraer porcion especifica de la cadena "Slicing" string[start:stop]
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)

#Paso12 - Extraer otros segmentos
year_code =  employee_code[4:8]
initials = employee_code[9:11]
print(year_code, initials)

#Paso13 -  Extraer indices negativos -1 se refiere al último carácter, -2 se refiere al penúltimo carácter, y así sucesivamente.
last_three =  employee_code[-3:]
print(last_three)












