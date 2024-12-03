
'''
from save_all_contact import save_all_contact


def search_contact1(All_Contacts):
    search_name = input("Enter the contact name to search: ")
    if search_name in All_Contacts:
        print(search_name, "Contact number is", All_Contacts[search_name])
    else:
        print("Contact not found.")
        
    #for All_Contacts in search_name:
        #if All_Contacts['number'] == search_name:
            #print(search_name ,"Contact number is ",All_Contacts[search_name])
            #break
        #else:
            #print("Contact not found.")



    save_all_contact(All_Contacts)

    return All_Contacts

'''