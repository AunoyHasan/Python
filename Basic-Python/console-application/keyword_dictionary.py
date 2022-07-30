dictionary = {}    
    
def add_dictionary():
    try:
        filename = 'content.txt'
        with open(filename, 'a') as f:
            name = input("Keyword name: ")
            description = input("Description: ")
            dictionary[name] = description
            if name in dictionary:
                print(name, " added successfully.\n\n")
                for key, value in dictionary.items():  
                    f.writelines((key, " : ", value, "\n"))  
            else:
                print("Can not add, something went wrong")
            
    except FileNotFoundError:
        print(f"{filename} does not exist")
               
            

def display_dictionary():
    try:
        filename = 'content.txt'
        with open(filename, 'r') as f:
            for i in f:
                print(i)
            
    except FileNotFoundError:
        print(f"{filename} does not exist")        
 
def edit_dictionary():
    edit_key = input("Enter the keyword you want to edit : ")
    if edit_key in dictionary:
        option = input("What do you want to edit?\nkeyord or description, If keyword press k or if description press d :")
        if option == 'k' or option == 'K':
            edited_key = input("Enter the new keyword: ")
            dictionary[edited_key] = dictionary.pop(edit_key)
            print("Your updated dictionary")
            display_dictionary()
        elif option == 'd' or option == 'D':
            description = input("Enter description: ")
            dictionary[edit_key] = description
            print("Description updated. Your updated dictionary")
            display_dictionary()
        else:
            pass
    else:
        print(edit_key, "is not found in the dictionary\n\n")        
  
def delete_dictionary():
    delete_key = input("Enter the key that you want to delete : ")
    if delete_key in dictionary:
        confirm = input("Confirm delete y/n : ")
        if confirm == 'y' or confirm == 'Y':
            dictionary.pop(delete_key)
            print(delete_key, "has been deleted\n\n")
            display_dictionary()
        else:
            print(delete_key, "is not found in the dictionary \n\n")
 
def search_dictioanary():
    search_key = input("Enter the keyword you want to search : ")
    if search_key in dictionary:
        print(search_key, " key's description: ", dictionary[search_key])
    else:
        print(search_key, "is not found in the dictionary\n\n")
        option = input("Do you want to add this keyword y/n:")
        if option == 'y' or option == 'Y':
            description = input("Description of the keyword: ")
            dictionary[search_key] = description
            if search_key in dictionary:
                print(search_key, " added successfully.\n\n")
            else:
                print("Can not add, something went wrong")
        else:
            pass
 
while True:
    print("*************Dictionary for reserve keyword*******************")
    choise = int(input(" 1. Add new keyword \n 2. Search keyword \n 3. Display keyword list \n 4. Edit keyword \n 5. Delete keyword \n 6. Exit \n ***Enter your choise : "))
    
    if choise == 1:
        add_dictionary()
    
    elif choise == 2:
        search_dictioanary()
    
    elif choise == 3:
        display_dictionary()
    
    elif choise == 4:        
        edit_dictionary()
    
    elif choise == 5:
        delete_dictionary()
    
    elif choise ==6:
        break
        
    else:
        print("Wrong input chosen, please choose the correct input")
            