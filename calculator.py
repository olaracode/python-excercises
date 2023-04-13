# Primero declaramos nuestras funciones
# que son las opciones de la calculadora
suma = lambda a, b: a + b
resta = lambda a, b: a - b
multiplica = lambda a, b: a * b
dividir = lambda a, b: a // b

# Declaramos lo que define si 
# nuestra aplicacion esta corriendo o no
running = True

# Ejecutamos nuestra aplicacion
# Y se sigue ejecutando mientras running sea true
while running == True:
    # Que el usuario escoja una accion
    print("Opcion 0: Exit App")
    print("Opcion 1: Sumar")
    print("Opcion 2: Restar")
    print("Opcion 3: Multiplicar")
    print("Opcion 4: Dividir")

    # Escoje la accion
    # Y esa accion la volvemos un numero
    user_action = int(input("Escoja su operacion(1, 2, 3, 4): "))

    # Si escoje 0 terminamos nuestro bucle
    if user_action == 0:
        print("-" * 36)
        print("Vuelva pronto, gracias por usa mi calculadora")
        print("-" * 36)
        running = False
        break # Break termina el ciclo actual del loop
    
    # Recibimos los valores que el usuario quiere "operar"
    # Los convertimos en ints para poder hacer operaciones matematicas
    user_number_one = int(input("Ingrese el primer numero: "))
    user_number_two = int(input("Ingrese el segundo numero: "))
    
    # Dependiendo de la accion del usuario ejecutamos una operacion distinta
    if user_action == 1:
        print(f"Voy a sumar {user_number_one} y {user_number_two}: ")
        print(suma(user_number_one, user_number_two))
    elif user_action == 2:
        print(f"Voy a restar {user_number_one} y {user_number_two}")
        print(resta(user_number_one, user_number_two))
    elif user_action == 3:
        print(f"Voy a multiplicar {user_number_one} y {user_number_two}")
        print(multiplica(user_number_one, user_number_two))
    elif user_action == 4:
        print(f"Voy a dividir {user_number_one} y {user_number_two}")
        print(dividir(user_number_one, user_number_two))
    else:
        print("Escoja una opcion valida")
    print("-" * 36)