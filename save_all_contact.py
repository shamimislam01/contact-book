def save_all_contact(Contacts):
    with open('all_contacts.csv','w') as fp:
        for Contact in Contacts:
            line=(f"{Contact['name']},{Contact['number']},{Contact['email']},{Contact['address']}")
            fp.write(line)
            

