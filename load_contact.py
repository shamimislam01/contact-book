from contact_book import All_Contacts
import os

def load_contact(file_path="all_contacts.csv"):
    with open(file_path, "r") as file:
        for line in file:
            name, number, email, address = line.strip().split(",")
            load_contact.append({
                "name": name,
                "number": number,
                "email": email,
                "address": address
            })
    
    print("Contacts loaded successfully.")
    return load_contact
load_contact()