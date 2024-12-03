def view_all_contact(contact_list):
    if not contact_list:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contact_list, start=1):
            print(f"Contact {i}:")
            print(f"Name: {contact['name']}")
            print(f"Phone Number: {contact['number']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
