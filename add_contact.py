from save_all_contact  import save_all_contact

def add_contact(contact_list):
    name = input("Enter Your Name: ")
    while True:
        try:
            number = input("Enter Your Phone Number: ")
            if len(number) == 11:
                break
            else:
                print("Phone number must be 11 digits long. Please try again.")
        except ValueError as e:
            print(e)
            print("Please enter a valid phone number.")
       
    email = input("Enter Your Email: ")
    address = input("Enter Your Address: ")






    contact_list.append({
        "name": name,
        "number": number,
        "email": email,
        "address": address,
    })
    
    print("Contact added successfully.")

    save_all_contact(contact_list)

    return contact_list
