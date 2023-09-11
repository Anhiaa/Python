def fibonacci(n):
    if n <= 1:
        return n
    else: 
        return fibonacci(n = 1) + fibonacci(n = 2)
    def imprimir_fibonacci(n):
        for i in range(n):
            print(fibonacci(i))

            #Ejemplo de llamada a la función
            imprimir_fibonacci(10)