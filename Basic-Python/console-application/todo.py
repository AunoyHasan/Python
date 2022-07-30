my_todo_list = []

def my_list():
    try:
        filename = 'content.txt'
        with open(filename, 'r') as f:
            for i in f:
                print(i)
            
    except FileNotFoundError:
        print(f"{filename} does not exist")  
 
def add_todo():    
    try:  
        filename = 'content.txt'
        with open(filename, 'a') as f:
            new_todo = input("Enter the todo that you want to add : ").lower()
            my_todo_list.append(new_todo)
            if new_todo in my_todo_list:
                print(f"{new_todo} is added successfully")
                f.writelines((new_todo, "\n"))
    except FileNotFoundError:
        print(f"{filename} not found, something went wrong")
        
def search_todo():
    search_todo = input("Enter todo you want to search: ")
    if search_todo in my_todo_list:
        print(f"Your seach to is: {search_todo}")
    else:
        print(f"{search_todo} is not in the list")
        option = input("Do you want to add this {search_todo} y/n: ")
        if option == 'Y' or option == 'y':
            my_todo_list.append(search_todo)
            if search_todo in my_todo_list:
                print(f"{search_todo} added successfully")
            else:
                print("Can not add, something went wrong")
        elif option == 'N' or option == 'n':
            pass
        else:
            pass
            
def edit_todo():
    while True:
        item_name = input("Enter the todo name that you want to update: ").lower()
        try:
            if item_name in my_todo_list:
                update_item = input("Enter todo: ").lower()
                index = my_todo_list.index(item_name)
                my_todo_list[index] = update_item
                if update_item in my_todo_list:
                    print("Your todo is updated")
                    print("Your updated todo")
                    my_list()
                    break
                else:
                    print("Can not update, something went wrong")
            else:
                print(f"{item_name} is not found in todo list")
        except Exception:
            print("Something went wrong") 

def delete_todo():
    while True:
        delete_todo = input("Enter the todo that you want to delete : ").lower()
        try:
            if delete_todo in my_todo_list:
                confirm = input("Confirm delete y/n : ")
                if confirm == 'y' or confirm == 'Y':
                    my_todo_list.remove(delete_todo)
                    print(delete_todo, "has been deleted\n\n")
                    break
                else:
                    print(delete_todo, "is not found in the contact book \n\n")
        except Exception:
            print("Something went wrong")            
            

while True:
    try:
        print("*************ToDoSystem*******************")
        choise = int(input(" 1. Add new todo \n 2. Search todo \n 3. Display todo list \n 4. Edit todo \n 5. Delete todo \n 6. Exit \n ***Enter your choise : "))
    
        if choise == 1:
            add_todo()
        elif choise == 2:
            search_todo() 
        elif choise == 3:
            my_list() 
        elif choise == 4:        
            edit_todo()
        elif choise == 5:
            delete_todo()
        elif choise == 6:
            break
        else:
            pass
    except Exception:
        print("Something went wrong, please try agnain")