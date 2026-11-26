###  En este taller, practicarás escribir funciones reutilizables en Python y aplicar el ámbito local y global para crear un rastreador de inventario de cocina.

### Paso1  - Crea tres variables: available_eggs, available_flour y available_sugar
available_eggs = 1
available_flour = 2
available_sugar = 3

## Paso2  -  crear una función para verificar lo que tienes en tu cocina. crear una función para verificar lo que tienes en tu cocina. 

def check_kitchen_stock():
    pass

## Paso3  - Las funciones tienen su propio ámbito local. Esto significa que las variables creadas dentro de una función. Sin embargo, las funciones no están completamente aisladas. Pueden leer variables globales definidas afuera de su ámbito. Pueden usar esas variables para realizar cálculos, tomar decisiones o crear nuevas variables locales.Sin embargo, las funciones no están completamente aisladas. Pueden leer variables globales definidas afuera de su ámbito. Pueden usar esas variables para realizar cálculos, tomar decisiones o crear nuevas variables locales.

def check_kitchen_stock():
    total_items = available_eggs + available_flour + available_sugar

## Paso4 - mostrar el inventario. 

def check_kitchen_stock():
     total_items = available_eggs + available_flour + available_sugar
     print(f'The kitchen has {total_items} total items:')
     print(f'- {available_eggs} eggs')
     print(f'- {available_flour} flour')
     print(f'- {available_sugar} sugar')

## Paso5 - llamar (o invocar) la función.
check_kitchen_stock()

## Paso6 - crea una nueva función que acepte parámetros.

def use_eggs(available_eggs, eggs_to_use):
    pass

###############Ten en cuenta que si le das a un parámetro el mismo nombre que una variable global (como available_eggs), la función usará su propio parámetro local available_eggs en lugar del global. Esto se conoce como sombreado de nombres porque la variable local "ensombrece" a la global.

## Paso7 -  verificar si tienes suficientes huevos para cocinar. Puedes hacer esto usando una sentencia if.

def use_eggs(available_eggs, eggs_to_use):
    if eggs_to_use > available_eggs:
        print('The kitchen does not have enough eggs.')

## Paso8 - detener la ejecución de la función. Cuando una función encuentra una sentencia return, deja de ejecutarse inmediatamente y devuelve el valor retornado al lugar donde fue llamada.

def use_eggs(available_eggs, eggs_to_use):
    if eggs_to_use > available_eggs:
        print('The kitchen does not have enough eggs.')
        return available_eggs

## Paso9 - procesar tus datos y devolver un nuevo valor calculado.

def use_eggs(available_eggs, eggs_to_use):
    if eggs_to_use > available_eggs:
        print('The kitchen does not have enough eggs.')
        return available_eggs
    print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
    return available_eggs - eggs_to_use 


## Paso10 - Ahora que tu función use_eggs está completa, puedes probarla. Al llamar a una función que requiere parámetros, pasas los valores específicos dentro de los paréntesis. Estos valores se conocen como argumentos.

use_eggs(available_eggs,1) #1 egg(s) used out of 1 available.'

### Paso11 12 -  Una función puede llamar a otra función y usar su valor devuelto
print(available_eggs)

def make_fried_egg(available_eggs):
    pass

##Paso 13  -  Verificar si tienes los ingredientes requeridos. Puedes hacer esto comparando la cantidad disponible de huevos con la cantidad necesaria para la receta.
def make_fried_egg(available_eggs):
    has_enough_eggs  = available_eggs >= 1

##Paso14  -  La llamada anterior a use_eggs devolvió el número restante de huevos, pero no asignaste ese resultado a una variable. Esta vez, usarás el valor devuelto para actualizar el conteo local de huevos en make_fried_egg. Para actualizar realmente tu inventario, necesitas capturar ese valor devuelto asignándolo a una variable.

def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1
    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)  
        print('Made a fried egg. Yummy!')
    else:
        print('Could not make a fried egg. Not enough eggs!')

##Paso15 - Tu función make_fried_egg ahora verifica si hay un huevo disponible y actualiza su conteo local de huevos cuando se usa uno. A continuación, devuelve ese conteo para que pueda usarse afuera de la función.

def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1
    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)  
        print('Made a fried egg. Yummy!')
    else:
        print('Could not make a fried egg. Not enough eggs!')
    return(available_eggs)

##Paso16 - Ahora, asigna el valor devuelto a la variable global para actualizar tu inventario. Recuerda que los parámetros de función son variables locales. Cuando pasas la variable global available_eggs a make_fried_egg, su parámetro local inicialmente se refiere al mismo entero. 

available_eggs = make_fried_egg(available_eggs)

##Paso17 -  check_kitchen_stock() Revisa tu inventario de cocina una última vez para verificar que el número de huevos realmente haya disminuido. Al final de tu código, llama de nuevo a la función check_kitchen_stock(). Cuando ejecutes el código, deberías ver que la cocina ahora tiene 0 huevos.

check_kitchen_stock()


