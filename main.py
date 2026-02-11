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
        ans = input('Add or remove? ')
        while ans == 'add' or 'Add':
            a = input('What would you like to add?: ') 
            to_do_list.append(a)
            print(to_do_list)
            input('Do you want to add something else? ')
            if 'yes' or 'Yes':
                continue
            if 'no' or 'No':
                break
    else:
        print("Make sure to finish your current tasks and come back when you finish one to update your list!")


lists(to_do_list)




# def add_remove(to_do_list):