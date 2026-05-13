# Generador de contrasenas seguras
import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """Genera una contrasena aleatoria con los criterios especificados."""
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = []

    # Garantizar al menos un caracter de cada tipo seleccionado
    password.append(random.choice(string.ascii_lowercase))
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Rellenar el resto de la contrasena
    remaining = length - len(password)
    password.extend(random.choice(characters) for _ in range(remaining))

    # Mezclar para que los caracteres garantizados no esten siempre al inicio
    random.shuffle(password)

    return ''.join(password)

def check_strength(password):
    """Evalua la fortaleza de una contrasena."""
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    levels = {0: "Very Weak", 1: "Weak", 2: "Fair",
              3: "Moderate", 4: "Strong", 5: "Very Strong", 6: "Excellent"}
    return levels.get(score, "Excellent")

print("--- Password Generator ---\n")

try:
    length = int(input("Password length (default 12): ") or "12")
except ValueError:
    length = 12

use_upper = input("Include uppercase? (y/n, default y): ").lower() != 'n'
use_digits = input("Include digits? (y/n, default y): ").lower() != 'n'
use_symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'

count = 5
print(f"\nGenerated {count} passwords:\n")
for i in range(count):
    pwd = generate_password(length, use_upper, use_digits, use_symbols)
    strength = check_strength(pwd)
    print(f"  {i + 1}. {pwd}  [{strength}]")
