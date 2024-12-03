from add_contact import add_contact
from view_all_contact import view_all_contact
from remove_contact import remove_contact
#from search import search_contact1

All_Contacts = []
load_contact=[]
while True:
    print("Contact Book Management System.")
    print("0. Exit")
    print("1. Add Contacts")
    print("2. View Contacts")
    print("3. Remove Contacts")
    print("4. Search Contacts")
    try:
        choice = int(input("Enter your Choice Number: "))
    except ValueError:
            print("Invalid input! Choice must be an integer. Please try again.")
            continue

    if choice == 0:
        print("Thanks for using Contact Book Management System")
        break
    elif choice == 1:
        All_Contacts = add_contact(All_Contacts)
    elif choice == 2:
        view_all_contact(All_Contacts)
    elif choice == 3:
        All_Contacts = remove_contact(All_Contacts)
        
        
    elif choice == 4:
        #All_Contacts = search_contact1(All_Contacts)
        '''
        search_name = input("Enter the contact name to search: ")
        if search_name in All_Contacts:
            print(search_name, "Contact number is", All_Contacts[search_name])
        else:
            print("Contact not found.")
         '''
    else:
        print("Invalid Choice Number")
