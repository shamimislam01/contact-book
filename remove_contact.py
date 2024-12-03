from save_all_contact import save_all_contact

def remove_contact(contact_list1):
    remove_input = input("Enter the phone number of the contact to remove: ")

    # Find and remove the contact by phone number
    for contact in contact_list1:
        if contact['number'] == remove_input:
            contact_list1.remove(contact)
            print("Contact removed successfully.")
            break
    else:
        print("Contact not found.")


    save_all_contact(contact_list1)
    return contact_list1

