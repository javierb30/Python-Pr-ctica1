from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
correcto = 0
incorrecto = 0
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Hola! ¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    while (operator == "/") and (number_2 == 0):
        #Si llega el caso de una division por cero, busco otro numero
        number_2 = randrange(10)
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = int(input("resultado: "))
    match operator:
        case '+' : 
            valor = number_1 + number_2
        case '-' :
            valor = number_1 - number_2
        case '*' :
            valor = number_1 * number_2
        case '/' :
            valor = number_1 / number_2 
    if valor == result :
        correcto += 1
        print("Respuesta correcta")
    else:
        incorrecto += 1
        print("Respuesta incorrecta")
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print("Respuestas correctas: " , correcto)
print("Respuestas incorrectas: " , incorrecto)