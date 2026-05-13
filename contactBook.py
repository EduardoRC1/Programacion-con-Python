# Agenda de contactos usando diccionarios
contacts = {}

def show_menu():
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Show all contacts")
    print("5. Exit")

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")

def show_all():
    if not contacts:
        print("No contacts saved.")
        return
    print(f"\n{'Name':<20} {'Phone':<15} {'Email':<25}")
    print("-" * 60)
    for name, info in contacts.items():
        print(f"{name:<20} {info['phone']:<15} {info['email']:<25}")

while True:
    show_menu()
    choice = input("Choose an option: ").strip()
    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        show_all()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
