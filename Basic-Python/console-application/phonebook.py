contact = []

def add_contact():
    file_name = 'content.txt'
    try:
        with open(file_name, 'a') as file_object:
            name = input("Enter the contact name : ")
            address = input("Enter the contact address : ")
            email = input("Enter the contact email : ")
            phone = input("Enter the phone phone : ")
            contact = [name, '|' , address, '|', email, '|', phone]
            if name in contact:
                file_object.writelines(contact)
                file_object.write('\n')
                print(name, " added successfully.\n\n")
            else: 
                print("Can not add, something went wrong")
    except FileNotFoundError:
        print(f"{filename} not found, something went wrong")
        
def search_contact():
    search_name = input("Enter the name you want to search : ")
    if search_name in contact:
        print(f"Your seach to is: {search_name}")
    else:
        print(f"{search_name} is not in the list")
        option = input("Do you want to add this {search_name} y/n: ")
        if option == 'Y' or option == 'y':
            my_todo_list.append(search_todo)
            if search_name in contact:
                print(f"{search_name} added successfully")
            else:
                print("Can not add, something went wrong")
        elif option == 'N' or option == 'n':
            pass
        else:
            pass    

def display_contact():
    file_name = 'content.txt'
    try:
        with open(file_name, 'r') as file_object:
            for i in file_object:
                print(i)
    except FileNotFoundError:
        print(f"{filename} not found, something went wrong")
        
def edit_contact():
    while True:
        item_name = input("Enter the contact name that you want to update: ").lower()
        try:
            if item_name in contact:
                update_item = input("Enter name: ").lower()
                index = my_todo_list.index(item_name)
                contact[index] = update_item
                if update_item in my_todo_list:
                    print("Your contact has been updated")
                    print("Your updated contact book")
                    display_contact()
                    break
                else:
                    print("Can not update, something went wrong")
                    break
            else:
                print(f"{item_name} is not found in contact list")
        except Exception:
            print("Something went wrong") 
            
def delete_contact():
    del_contact = input("Enter the contact that you want to delete : ")
    if del_contact in contact:
        confirm = input("Confirm delete y/n : ")
        if confirm == 'y' or confirm == 'Y':
            contact.remove(del_contact)
            print(del_contact, "has been deleted\n\n")
            display_contact()
        else:
            print(del_contact, "is not found in the contact book \n\n")

while True:
    try:
        print("*************Phone Book Management System*******************")
        choise = int(input(" 1. Add new contact \n 2. Search contact \n 3. Display contact \n 4. Edit contact \n 5. Delete Contact \n 6. Exit \n ***Enter your choise : "))
    
        if choise == 1:
            add_contact()
    
        elif choise == 2:
            search_contact()
    
        elif choise == 3:
            display_contact()
            
        elif choise == 4:        
            edit_contact()
    
        elif choise == 5:
            delete_contact()
    
        elif choise == 6:
            break
        else:
            print("Wrong input taken, please try agian")
            pass
    except Exception:
        print("Something went wrong, please try again")
          