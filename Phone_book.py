import csv
from collections import defaultdict
from colorama import *

reset = Style.RESET_ALL
wrng = Fore.RED + Style.BRIGHT
data = defaultdict(list)

data['raj'].append(8745169510)
data['shubham'].append(9595130613)
data['shubham'].append(9574012465)


def check_book():
    if not bool(data):
        return True
    return False


def clear_screen():
    print('\n' * 25)


def add_contact():
    while True:
        name = input('Enter name >>')
        mobile_no = input('Enter mobile no >>')
        if mobile_no.isdigit():
            data[name]= mobile_no
            save()
            cmd = input(Fore.LIGHTGREEN_EX +'create more contact \'Y\' or \'N\' ?\n>>').lower()
            print(reset+ '')
            if cmd == 'y':
                pass
            else:
                break

        else:
            print(Fore.RED + Style.BRIGHT + "Mobile no contains only number\'s \n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",end="")
            print(reset)


def find(cust):
    if cust in data.keys():
        return True
    return False


def find_contact():
    while True:
        res =""
        key = input('enter contact name to search \n>>')

        res = dict(filter(lambda item: key.casefold() in item[0], data.items()))
        if res == {}:
            print(wrng + 'No contact found..!')
        else:
            print(Fore.GREEN , res)
            print(reset)


def delete_contact():
    cmd = input(Fore.RED + "Enter contact name to delete\n>>")

    if cmd in data.keys():
        print(Fore.LIGHTGREEN_EX + 'contact deleted,', cmd, data.pop(cmd))
        save()
    else:
        print('no contact found..')


def show_contact():
    if data =={}:
        print(wrng + "No contact to display....!")
    else:
        for contact in data:
            print(Back.LIGHTBLACK_EX + Fore.GREEN + f'{contact} {data[contact]}')
        print(Style.RESET_ALL,end="")
        print("**********************************************")



def edit_contat():
    show_contact()
    cmd = input(Fore.GREEN + "Enter contact name to edit\n>>")
    if cmd in data:
        task = input("edit name or no..?")
        if task.lower() == "no":
            no = int(input("Enter new no \n>> "))
            updated = {cmd: no}
            data.update(updated)

        elif task.lower() == "name":
            name = input("Enter new name ")
            no = data[cmd]
            data.pop(cmd)
            data.update({name: no})
        else:
            print(Fore.RED + "Enter valid input")

    else:
        print(Fore.RED + "NO CONTACT FOUND")
    print(Style.RESET_ALL)

def save():
    w = csv.writer(open("output.csv", "w"))
    for key, val in data.items():
        w.writerow([key, val])





if __name__ == '__main__':

    with open('output.csv') as f:
        data = dict(filter(None, csv.reader(f)))


    while True:
        name = '\"Shubham\'s phoneBook\"'
        new = name.center(40, '-')
        print(Fore.RED + new)

        print(Fore.BLUE + '1) Add a new contact\n'
                          '2) delete a contact\n'
                          '3) search a contact\n'
                          '4) Show all contacts\n'
                          '5) Add a existing to contact\n'
                          "6) Edit Contact no \n"
                          "7) clear screen"

              )
        print(Fore.RED + '-------------------------------------------')
        print(Style.RESET_ALL, end="")
        cmd = int(input(Fore.RED + Style.BRIGHT + 'Select >>>'))
        print(Style.RESET_ALL, end="")

        if cmd == 1:
            add_contact()
        elif cmd == 2:
            if check_book():
                print(Fore.RED + "phone book is empty")

            else:
                delete_contact()

        elif cmd == 3:
            if check_book():
                print(Fore.RED + "phone book is empty")

            else:
                find_contact()

        elif cmd == 4:
            show_contact()
        elif cmd == 5:
            add_contact()
        elif cmd == 6:
            edit_contat()
        elif cmd == 7:
            clear_screen()

        else:
            print(Fore.RED + Style.BRIGHT + "try valid option")

            print(Style.RESET_ALL + '_______________________')
