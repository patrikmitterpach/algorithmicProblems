def productFib(product):
    Fib1 = 0
    Fib2 = 1

    while Fib1 * Fib2 < product:
        Fib1, Fib2 = Fib2, Fib1+Fib2

    return [Fib1, Fib2, Fib1 * Fib2 == product]

print( productFib(5895) )