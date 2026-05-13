# Manejo de errores con try/except

# Division segura
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Both arguments must be numbers."
    return result

print("--- Safe Division ---")
print(f"10 / 3 = {safe_divide(10, 3)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'a' = {safe_divide(10, 'a')}")

# Validacion de entrada del usuario
def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("That's not a valid integer. Try again.")

# Acceso seguro a listas
def safe_list_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Error: Index {index} is out of range (list has {len(lst)} elements)."

print("\n--- Safe List Access ---")
my_list = [10, 20, 30, 40, 50]
print(f"Index 2: {safe_list_access(my_list, 2)}")
print(f"Index 10: {safe_list_access(my_list, 10)}")

# Acceso seguro a diccionarios
def safe_dict_access(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return f"Error: Key '{key}' not found."

print("\n--- Safe Dict Access ---")
student = {"name": "Maria", "age": 20, "grade": "A"}
print(f"Name: {safe_dict_access(student, 'name')}")
print(f"Phone: {safe_dict_access(student, 'phone')}")

# Bloque try/except/else/finally
print("\n--- Complete Error Handling ---")
try:
    num = get_integer("Enter a number to divide 100 by: ")
    result = 100 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"100 / {num} = {result}")
finally:
    print("Operation complete.")
