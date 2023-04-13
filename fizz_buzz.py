# Debe imprimir de 0 a 100, si el numero es divisible entre 3 debe imprimir Fizz, si es divisible entre 5 debe imprimir Buzz, si es divisible entre 3 y 5 debe imprimir FizzBuzz, si no es divisible entre 3 o 5 debe imprimir el numero

for i in range(101):
    if(i == 0):
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)