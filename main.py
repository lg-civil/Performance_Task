# Purpose: A to-do list that let's the user add or remove tasks 


# Starter List
to_do_list = ["Homework", 'Walk the Dog', 'Wash dishes']

# Asks the user for their name and explains that they can add or remove items to the list
def intro():
    name = input('Hello, what is your name? ')
    print(f"Hello {name}. This is a list of things you need to finish. It currently holds three tasks but if they don't apply to you, you can choose to add new ones or remove the current ones. ")
    print(to_do_list)

# Calls the functions
intro()



def remove():
    # Asks the user if they want to remove something from the list
    ans = input('Do you want to remove something? (yes/no) ').lower()
    while ans == 'yes':
    # While the answer is 'yes', the user is asked to enter what task from the list they want to remove
        a = input('What would you like to remove?: ')
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
        elif not to_do_list:
            k = input('List is empty. Do you want to add something?').lower()
            if k == 'yes':
                lists(to_do_list)
            elif k == 'no':
                print('Great job. You finished your tasks.')

# Defines the function and includes a parameter which is the starter list
def lists(to_do_list):
# Asks user if they want to add something to the list 
    answer = input("Is there anything you want to add? (yes/no) ")
# If the user says yes, while that condition remains true, the follwing steps are followed
    if answer == "yes":
        while answer == 'yes':
# Asks user what they want to add to the list
            a = input('What would you like to add?: ') 
# Adds the users input to the list
            to_do_list.append(a)
# Prints the new list
            print(to_do_list)
# Asks the user is they want to add another item to the list and also gives them the option to remove
            n = input('Do you want to add something else? (if you want to remove something type the word "remove" ) ').lower()
# If the user wants to keep adding items to the list, the list continues
            if n == 'yes':
                  continue
# If the user doesn't want to add or remove anything to the list, they are told to finish their current tasks and the loop ends
            elif n == 'no':
                print('Ok go on and finish your list of things!')
                break
# If the user wants to remove an item from the list, the loop is broken and the function "remove" is called
            elif n == 'remove':
                remove()
                break
# If the user originally decided not to add anything new to the list the following steps are followed
    elif answer == 'no':
# Because the user decided not to add anything, they are asked if there is something from the list that they want to remove
         w = input('Would you like to remove something? ')
# If the user says yes, the function "remove" is called
         if w == 'yes':
             remove()
# If the user says no they are told to finish their current tasks and return whenever they would like to update their list
    elif w == 'no':
        print("Make sure to finish your current tasks and come back when you finish one to update your list!")


# Calls the program and runs it
lists(to_do_list)