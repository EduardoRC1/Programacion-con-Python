# Ejemplos de list comprehensions y operaciones con listas

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Cuadrados de cada numero
squares = [n ** 2 for n in numbers]
print("Squares:", squares)

# Filtrar solo numeros pares
evens = [n for n in numbers if n % 2 == 0]
print("Evens:", evens)

# Filtrar numeros impares
odds = [n for n in numbers if n % 2 != 0]
print("Odds:", odds)

# Numeros pares al cuadrado
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print("Even squares:", even_squares)

# Nested list comprehension - tabla de multiplicar
multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("\nMultiplication Table (5x5):")
for row in multiplication_table:
    print(row)

# Aplanar una lista de listas
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = [item for sublist in nested for item in sublist]
print("\nFlattened:", flat)

# Filtrar palabras por longitud
words = ["python", "is", "a", "powerful", "programming", "language"]
long_words = [w for w in words if len(w) > 4]
print("Long words:", long_words)

# Crear un diccionario con comprehension
word_lengths = {w: len(w) for w in words}
print("Word lengths:", word_lengths)
