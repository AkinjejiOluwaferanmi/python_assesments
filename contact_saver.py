def save_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    with open("contacts.txt", "a") as file:
        file.write(f"{name} - {phone}\n")
    print("Contact saved successfully!")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.")
            else:
                for contact in contacts:
                    print(contact.strip())
    except FileNotFoundError:
        print("No contacts found.")

def main():
    while True:
        print("\nSimple Contact Saver")
        print("1. Save contact")
        print("2. View all contacts")
        print("3. Exit")
        choice = input("Enter choice (1-3): ")
        
        if choice == "1":
            save_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()