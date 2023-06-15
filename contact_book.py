import csv

from constants import CONTACT_FILE

def load_contact():
    try:
        with open(CONTACT_FILE,'r') as read_file:
            reader=csv.reader(read_file)
            contacts=list(reader)
    except FileNotFoundError:
        print("file was not found")
        contacts = {}
        print(contacts)
    return contacts

def save_contact(contacts):
    with open(CONTACT_FILE,'w',newline='') as write_file:
        writer=csv.writer(write_file)
        for rows in contacts:
            writer.writerow(rows)

def display_contacts(contacts):
    # if contacts:
    #     for dataitems in contacts:
    #         print("NAME:", dataitems[0],"  NUMBER:",dataitems[1])
    # else:
    #     print('Contact not found')
    if not contacts:
        print('NO contacts found')
        return
    else:
        print("CONTACTS:")
        for dataitems in contacts:
            print("NAME:", dataitems[0], "  NUMBER:", dataitems[1])

def add_contact():
    name = input("ENTER CONTACT NAME: ")
    phone = input("ENTER CONTACT PHONE NUMBER {add only 10 digit no}: ")
    new_contact=[name,phone]
    with open(CONTACT_FILE,'a',newline='') as append_file:
        append=csv.writer(append_file)
        append.writerow(new_contact)
    print('Contact added successfully')

def delete_contact(contacts):
    delete_user_input = input("ENTER CONTACT NAME TO DELETE: ")
    for dataitems in contacts:
        if dataitems[0]==delete_user_input:
            print('CONTACT NAME FOUND')
            contacts.remove(dataitems)
            print('DELETED')
            save_contact(contacts)


def search_contact(contacts):
    search_user_input = input("Enter any name to be search in contact list: ")
    for dataitem in contacts:
        if dataitem[0]==search_user_input:
            print("Search found")
            print(f" NAME:{dataitem[0]}   NUMBER:{dataitem[1]}")


def main():
    while True:
        contacts = load_contact()
        print('\n____CONTACT BOOK_____')
        print('1. Display all contacts')
        print('2. Add a new contact')
        print('3. Delete a contact')
        print('4. Search for a contact')
        print('5. Exit the application')
        user_input=int(input('Enter ur no. here: '))

        if user_input==1:
            display_contacts(contacts)
        elif user_input==2:
             add_contact()
        elif user_input==3:
            delete_contact(contacts)
        elif user_input==4:
            search_contact(contacts)
        elif user_input == 5:
            print('exit')
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()



