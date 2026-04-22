to_do_list = ["Homework", 'Walk the Dog', 'Wash dishes']

def intro():
    name = input('Hello, what is your name? ')
    print(f"Hello {name}. This is a list of things you need to finish. It currently holds three tasks but if they don't apply to you, you can choose to add new ones or remove the current ones. ")
    print(to_do_list) 
intro()

def remove():
    ans = input('Do you want to remove something? (yes/no) ').lower()
    while ans == 'yes':
        a = input('What would you like to remove? Type it as it is in the list!: ')
        to_do_list.remove(a)
        print(to_do_list)
        if not to_do_list:
            k = input('List is empty. Do you want to add something? ' ).lower()
            if k == 'yes':
                lists(to_do_list)
            elif k == 'no':
                print('Great job. You finished your tasks.')
                break
        n = input('Do you want to remove something else? (yes/no) (if you want to add something say "add") ').lower()
        if n == 'yes':
            continue   
        elif n == 'no':
            print('Ok go on and finish your list of things!')
            break   
        elif n == 'add':
            lists(to_do_list)
            break
    while ans == 'no':
        print('Ok go on and finish your list of things!')
        break


def lists(to_do_list):
    answer = input("Is there anything you want to add? (yes/no) ")
    if answer == "yes":
        while answer == 'yes':
            a = input('What would you like to add?: ') 
            to_do_list.append(a)
            print(to_do_list)
            n = input('Do you want to add something else? (yes/no) (if you want to remove something type the word "remove" ) ').lower()
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
             print('Ok go on and finish your list of things!')             
lists(to_do_list)