# Secuencia de Fibonacci: recursiva vs iterativa

def fibonacci_recursive(n):
    """Calcula el n-esimo numero de Fibonacci de forma recursiva."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    """Calcula el n-esimo numero de Fibonacci de forma iterativa."""
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_sequence(n):
    """Genera los primeros n numeros de Fibonacci."""
    sequence = []
    for i in range(n):
        sequence.append(fibonacci_iterative(i))
    return sequence

n = int(input("How many Fibonacci numbers do you want? "))

print(f"\nFirst {n} Fibonacci numbers: {fibonacci_sequence(n)}")
print(f"\nFibonacci({n}) using recursion: {fibonacci_recursive(n)}")
print(f"Fibonacci({n}) using iteration: {fibonacci_iterative(n)}")
