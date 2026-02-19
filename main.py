# Purpose: A to-do list that let's the user add or remove tasks 


# Starter List
to_do_list = ["Homework", 'Walk the Dog', 'Wash dishes']

# Asks the user for their name and explains that they can add or remove items to the list
def intro():
    name = input('Hello, what is your name? ')
    print(f"Hello {name}. This is a list of things you need to finish. It currently holds three tasks but if they don't apply to you, you can choose to add new ones or remove the current ones. ")
    print(to_do_list)

# Calls the function
intro()



def remove():
    # Asks the user if they want to remove something from the list
    ans = input('Do you want to remove something? (yes/no) ').lower()
    while ans == 'yes':
    # While the answer is 'yes', the user is asked to enter what task from the list they want to remove
        a = input('What would you like to remove?: ') 
    # Removes the item they enter
        to_do_list.remove(a)
    # Prints the new list
        print(to_do_list)
    # Asks the user if they want to remove something else or if they want to add something to the list
        n = input('Do you want to remove something else? (if you want to add something say "add") ').lower()
    # If the user wants to keep removing items from the list, the loop continues
        if n == 'yes':
            continue
    # If the user doesn't want to remove or add anything to the list, the loop is broken and they are told to finish the tasks that their list currently holds
        elif n == 'no':
            print('Ok go on and finish your list of things!')
            break    
    # If the user wants to add something to their list, the loop is broken and a new function is called
        elif n == 'add':
            lists(to_do_list)
            break



def lists(to_do_list):
    answer = input("Is there anything you want to add? (yes/no) ")
    if answer == "yes":
        while answer == 'yes':
            a = input('What would you like to add?: ') 
            to_do_list.append(a)
            print(to_do_list)
            n = input('Do you want to add something else? (if you want to remove something type the word "remove" ) ').lower()
            if n == 'yes':
                  continue
            elif n == 'no':
                print('Ok go on and finish your list of things!')
                break
            elif n == 'remove':
                remove()
                break
    elif answer == 'no':
         w = input('Would you like to remove something? ')
         if w == 'yes':
             remove()
    elif w == 'no':
        print("Make sure to finish your current tasks and come back when you finish one to update your list!")


lists(to_do_list)