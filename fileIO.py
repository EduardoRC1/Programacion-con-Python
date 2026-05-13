# Lectura y escritura de archivos
import os

FILENAME = "notes.txt"

def write_notes(filename, notes):
    """Escribe una lista de notas en un archivo."""
    with open(filename, 'w') as f:
        for i, note in enumerate(notes, 1):
            f.write(f"{i}. {note}\n")
    print(f"Saved {len(notes)} notes to '{filename}'.")

def read_notes(filename):
    """Lee y muestra las notas de un archivo."""
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist yet.")
        return []

    with open(filename, 'r') as f:
        lines = f.readlines()

    notes = [line.strip() for line in lines if line.strip()]
    return notes

def append_note(filename, note):
    """Agrega una nota al final del archivo."""
    with open(filename, 'a') as f:
        count = len(read_notes(filename))
        f.write(f"{count + 1}. {note}\n")
    print(f"Note added: '{note}'")

def count_words(filename):
    """Cuenta las palabras en un archivo."""
    if not os.path.exists(filename):
        return 0
    with open(filename, 'r') as f:
        content = f.read()
    return len(content.split())

# Demo
print("--- File I/O Demo ---\n")

sample_notes = [
    "Learn Python basics",
    "Practice list comprehensions",
    "Study object-oriented programming",
    "Build a project with file I/O",
    "Review error handling"
]

write_notes(FILENAME, sample_notes)

print("\nReading notes:")
for note in read_notes(FILENAME):
    print(f"  {note}")

append_note(FILENAME, "Explore Python modules")

print(f"\nTotal words in file: {count_words(FILENAME)}")

# Limpiar archivo creado
os.remove(FILENAME)
print(f"\nCleaned up '{FILENAME}'.")
