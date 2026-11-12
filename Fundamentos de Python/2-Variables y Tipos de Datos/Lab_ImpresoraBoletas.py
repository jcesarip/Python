#En este taller, practicarás los tipos de datos de Python creando e imprimiendo datos para una boleta de calificaciones sencilla.

#Paso 1 - Definir Variable.
name = "Alice";
#Paso2 -  Imprirmir Valor de la Variable.
print(name); #"Alice"
#Paso3 - Verificar tipo valor de la variable.
print(type(name)); #<class 'str'>
#Paso4  -  Agrega el estado de inscripción del estudiante a los datos de la boleta con dato boleano.
is_student = True;
#Paso5 - mostrar más de un valor a la vez.
print(is_student, type(is_student)); #mostrar más de un valor a la vez.
#Paso6 - mostrar más de un valor a la vez.
print(name, type(name)); #Alice <class 'str'>
#Paso7 -  agrega la edad del estudiante a los datos de la boleta de calificaciones, Luego, imprime el valor y el tipo de dato de age
age = 20;
print(age,type(age)); #20 <class 'int'>
#Paso8 - añade la puntuación del estudiante.
score = 80.5;
print(isinstance(score,int)); #False
#Paso9 - Otro tipo común de número en Python es float, que representa un número con decimales. 
print(isinstance(score,float)); #True
#Paso10 - Imprime el valor de score junto con su tipo de dato usando una sola sentencia print()
print(score, type(score)); #80.5 <class 'float'>
