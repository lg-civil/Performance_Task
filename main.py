# to-do list

to_do_list = ["Homework", 'Walk the Dog', 'Eat Pizza']

def intro():
    name = input('Hello, what is your name? ')
    print(f"Hello {name}. This is a list of things you need to finish. It currently holds three tasks but if they don't apply to you you can choose to add or remove them. ")
    print(to_do_list)

intro()

def lists(to_do_list):
    answer = input("Is there anything you want to add or remove? (yes/no) ")
    if answer == "yes":
        ans = input('Add or remove? ').lower()
        if ans == 'add':
            while ans == 'add':
                a = input('What would you like to add?: ') 
                to_do_list.append(a)
                print(to_do_list)
                n = input('Do you want to add something else? (if you wantr to remove something type the word "remove" ) ').lower()
                if n == 'yes':
                    continue
                elif n == 'no':
                    print('Ok go on and finish your list of things!')
                    break
                elif n == 'remove':
                    lists(to_do_list)
        elif ans == 'remove':
            while ans == 'remove':
                ab = input('What would you like to remove?: ') 
                to_do_list.remove(ab)
                print(to_do_list)
                n = input('Do you want to remove something else? (if you want to add something type the word "add") ').lower()
                if n == 'yes':
                    continue
                elif n == 'no':
                    print('Ok go on and finish your list of things!')
                    break
                elif n == 'add':
                    lists(to_do_list)

    else:
        print("Make sure to finish your current tasks and come back when you finish one to update your list!")


lists(to_do_list)




# def add_remove():
#     answer = input("Is there anything you want to add or remove? (yes/no) ").lower()
#     if answer == 'yes':
#         ans = input('Add or remove? ').lower()
#         if ans == 'add':
#             while ans == 'add':
#                 a = input('What would you like to add?: ') 
#                 to_do_list.append(a)
#                 print(to_do_list)
#                 n = input('Do you want to add something else? ').lower()
#                 if n == 'yes':
#                     continue
#                 elif n == 'no':
#                     break
#             print('Ok go on and finish your list of things!')
#         elif ans == 'remove':
#             while ans == 'remove':
#                 a = input('What would you like to remove?: ') 
#                 to_do_list.remove(a)
#                 print(to_do_list)
#                 n = input('Do you want to remove something else? (if you want to add something say "add") ').lower()
#                 if n == 'yes':
#                     continue
#                 elif n == 'no':
#                     print('Ok go on and finish your list of things!')
#                     break    
#                 elif n == 'add':
#                     add_remove()
