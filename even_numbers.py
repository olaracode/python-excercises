# Una funcion que verifique si un elemento es par
# Otra funcion que agarre una lista y retorne solamente los elementos par
# Que la funcion even_elements reciba un parametro aparte
# El otro parametro es si va a regresar los pares o los impares

def is_even(number):
    # True | False
    return number % 2 == 0
test_numbers = range(11)

def even_elements_of_list(numbers, odd):
    even_numbers = []
    odd_numbers = []
    for number in numbers:
        # even es una variable
        # is_even es una funcion que retorna True | False
        even = is_even(number)
        if even:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    if odd == True:
        print("ODD:", odd_numbers)
        return odd_numbers
    else:
        print("EVEN:", even_numbers)
        return even_numbers

even_elements_of_list(test_numbers, True)
# even_elements_of_list(test_numbers, False)
