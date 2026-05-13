# Decoradores en Python
import time

def timer(func):
    """Decorador que mide el tiempo de ejecucion de una funcion."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"  [{func.__name__}] executed in {elapsed:.4f}s")
        return result
    return wrapper

def repeat(n):
    """Decorador que ejecuta una funcion n veces."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

def validate_positive(func):
    """Decorador que valida que los argumentos sean positivos."""
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Negative value not allowed: {arg}")
        return func(*args, **kwargs)
    return wrapper

# Uso de decoradores

@timer
def slow_sum(n):
    """Suma los numeros de 1 a n de forma lenta."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

@repeat(3)
def greet(name):
    """Saluda a alguien."""
    message = f"Hello, {name}!"
    print(f"  {message}")
    return message

@validate_positive
@timer
def calculate_area(width, height):
    """Calcula el area de un rectangulo."""
    return width * height

print("--- Timer Decorator ---")
result = slow_sum(1_000_000)
print(f"  Sum of 1 to 1,000,000 = {result}\n")

print("--- Repeat Decorator ---")
greet("Python")
print()

print("--- Validate + Timer Decorators ---")
area = calculate_area(5, 10)
print(f"  Area: {area}\n")

print("--- Validation Error ---")
try:
    calculate_area(-3, 10)
except ValueError as e:
    print(f"  Caught error: {e}")
