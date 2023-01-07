#This function gives the first N Fibonacci numbers, based on the user's input.

def fibonacci(N = int, fibonacci = [0, 1]):    #Definition of the amount of Fibonacci Numbers, and the fibonacci list itself.
    N = int(input('Fibonacci sequence until the N-th number.\n N = '))    #Constraint to natural numbers
    while N < 0:    #User input for N, defined previousy
        N = input(int('Invalid number. Only positive numbers. Try again'))  
    while len(fibonacci) <= N:    #Constraint to the list size
        fibonacci.append(fibonacci[-1] + fibonacci[-2])     #Appending the numbers, according to the Fibonacci Sequence
    fibonacci.pop(0)     #Removal of the number zero
    return print("Here's the first {} Fibonacci numbers:\n {}".format(N, fibonacci))

fibonacci()