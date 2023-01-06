# This function gives the first N Fibonacci numbers, based on the user's input.

def fibonacci(fibonacci = [0, 1]):
    N = int(input('Fibonacci sequence until the N-th number.\n N = '))
    while N < 0:
        N = input(int('Invalid number. Only positive numbers. Try again'))
    while len(fibonacci) <= N:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    fibonacci.pop(0)
    return print("Here's the first {} Fibonacci numbers:\n {}".format(N, fibonacci))

fibonacci()