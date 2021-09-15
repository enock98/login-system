#This function (create_user) is used to create a new user in the system. It also ensures that the previous entries are in the correct format, and that no double entries are made. This is called with user input "S"

from datetime import date
from datetime import datetime
from time import strptime


def create_user(): 
    print("Register new user.")
    with open("user.txt", "r") as readfile:
        existing_users_temp = readfile.readlines()
        
    with open("user.txt", "a+") as txtfile:
        
        existing_users = []
        
        for i in existing_users_temp:
            i = i.split(", ")
            existing_users.append(i)
        
        try:
            if "\n" not in existing_users[-1][1]:
                print("", file=txtfile)
        except:
            pass
        
        while True:
            existing_name = None
            username = input("Username: ")
            for i in existing_users:
                if i[0] == username:
                    print("User already exists, try another name.\n")
                    existing_name = i[0]
                    break
            if existing_name == username:
                continue

            while True:
                password = input("Password: ")
                passwordagain = input("Re-enter password: ")
                if password != passwordagain:
                    print("\nPasswords does not match, try again.\n")
                else:
                    break
            
            while True:
                store = input('\nDo you want to register user: "' + username + '"?').lower()
                if store == "y":
                    print(username + ", " + password, file=txtfile)
                    break
                elif store == "n":
                    print("\nMake a new entry:")
                    break
                else:
                    print("Enter (y)es or (n)o:")
                    continue
            if store == "y":
                break
                

# This function (user_login) is used to login a existing user in the user.txt file in the system. This is called with user input "L".
def user_login():
    
    with open("user.txt", "r") as task:
        contents = task.readlines()
        userlist = []
        for i in contents:
            i = i.replace("\n", "")
            i = i.split(", ")
            userlist.append(i)
        
    userpass = None

    while True:
        username = input("Username: ")
        password = input("Password: ")

        for i in userlist: 
            if username == i[0]:
                userpass = i[1]
                break
                
        else: 
            print("\nThe user does note exist, try again.\n")
            continue
                
        if userpass == password:
            print("Valid entry")
            break
            
        else:
            print("\nWrong password.\n")

    return username


#This function (printmenu1) is to print the menu in various conditions. The menu is changed depending on if a user is logged in or not, or if the admin-user is logged in.
def printmenu1(username):
    print()
    print("Do you want to:")
    
    if username == None:
        print("(L)ogin\t\t\t\t- L")
        
    if username == "admin":
        print("(R)egister a new user\t\t- R")
        print("(S)tatistics\t\t\t- S")
        print("(S)tatistics from (R)eports\t- SR")
        print("(M)ake (R)eport\t\t\t- MR")
    
    if username != None:
        print("(A)dd new task\t\t\t- A")
        print("(V)iew (A)ll tasks\t\t- VA")
        print("(V)iew (M)y tasks\t\t- VM")
        
    print("(Q)uit\t\t\t\t- Q")

    
#This function (menu1selector) is for taking inputs from the user. The inputs are restricted to be valid only for the choices that menu1 display for current user.
def menu1selector(username):
    while True:
        userinp = input("What do you want to do? ").lower()
        print()
        if userinp == "l" and username == None:
            username = user_login()
            return username
        
        elif userinp == "r" and username == "admin":
            create_user()
            return username
            
        elif userinp == "va" and username != None:
            viewall(username)
            return username
        
        elif userinp == "vm" and username != None:
            viewmytasks(username)
            return username
        
        elif userinp == "a" and username != None:
            usertask()
            return username
            
        elif userinp == "s" and username == "admin":
            taskstat()
            return username
        
        elif userinp == "sr" and username == "admin":
            print_reports()
            return username
            
        elif userinp == "mr" and username == "admin":
            make_reports()
            return username
        
        elif userinp == "q":
            quit()
            
    
        else:
            print("Enter a valid input")


#This function (viewall) is used to view all tasks in list. When this functions is called it opens the "tasks.txt" file and prints the item at index 2 (item no.3) of all entries in the file. This function is called when user inputs "VA" from the menu.

def viewall(username):
    with open("tasks.txt", "r") as taskfile:
        entries = taskfile.readlines()
        entries_list = []
        for i in entries:
            i = i.replace("\n", "")
            if i == "":
                continue
            i = i.split(", ")
            
            if len(i) < 1:
                continue
            entries_list.append(i)
            
    count = 1
    for i in entries_list:
        try:
            print(f"{count}: {i[2]}\n")
        
        except:
            print("fault")
            print(i)
        count += 1
        
    # new part, here we ask user what should be edidet an then call the function (edit_tasks()) that edits the part user chooses.

    #if username == "admin":
#        while True:
#            try:
#                task_choice = int(input("What task do you want to edit? "))
#                if task_choice == -1:
#                    break
#                elif 0 < task_choice <= count:
#                    task_choice -= 1
#                    if entries_list[task_choice][5] == "Yes":
#                        print("Unable - You can't edit completed tasks.")
#                        continue
#                    edit_tasks(task_choice)
#                    break
                
#                else:
#                    print("\nInvalid choice. Enter -1 to return to previous menu.")
#            except:
#                print("\nInvalid choice. Enter -1 to return to previous menu.dd")

# New part (edit_tasks) where the tasks may be edited. User, duedate and complete-status may be changed.

def edit_tasks(index):
    with open("tasks.txt", "r") as taskfile:
        entries = taskfile.readlines()
        entries_list = []
        for i in entries:
            i = i.replace("\n", "")
            if i == "":
                continue
            i = i.split(", ")
            
            if len(i) < 1:
                continue
            entries_list.append(i)
            
    task = entries_list.pop(index)
    print(f"1 - Name: {task[0]}")
    print(f"2 - Task: {task[1]}")
    print(f"3 - Description: {task[2]}")
    print(f"4 - Assigned date: {task[3]}")
    print(f"5 - Due date: {task[4]}")
    print(f"6 - Completed: {task[5]}")
    print()
    choice = input("What entry do you want to edit? ")
    
    if choice == "1":
        change = task.pop(0)
        print(f"Task currently assigned to {change}.")
        while True:
            changenew = input("Who do you want to assignt the task to? ")
            correct = input(f"Confirm you want to change this assignment to: {changenew}? (y/n)").lower()
            if correct == "y":
                change = changenew
                break
        task.insert(0,change)
        
    elif choice == "2" or choice == "3" or choice == "4":
        print("You can't change those entries.")

    elif choice == "5":
        change = task.pop(4)
        print(f"Current due-date is: {change}.")
        while True:
            
            try:
                a,b,c = input("Enter new due-date (ie. 31-12-2021): ").split("-")
            
                if int(c) < 2000:
                    print("insert a valid year with 4 numbers")
                    continue
                changenew = date(int(c), int(b), int(a))

            except:
                print("make sure to use format dd-mm-yyyy")
                continue
            
            changenew = changenew.strftime("%d %b %Y")
            correct = input(f"Confirm you want to change the due-date to: {changenew}? (y/n)").lower()
            if correct == "y":
                change = changenew
                break
            
        task.insert(4,change)
        
    
    elif choice == "6":
        if task[5] == "No":
            choice = input("The task is marked as incomplete, do you want to change it to complete?(y/n) ").lower()
            if choice == "y":
                change = task.pop(5)
                change = "Yes"
                task.insert(5, change)
            else:
                print("No change made.")
        
            
    entries_list.insert(index, task)
    
    with open("tasks.txt", "w+") as task:
             
        for i in entries_list:
            
            print(i[0] + ", " + i[1] + ", " + i[2] + ", " + i[3] + ", " + i[4] + ", " + i[5], file=task)
            print("", file=task)

        
    
    
    
#This function (viewmytasks) is used to view all tasks in the list that are assigned to the current user. When this functions is called it opens the "tasks.txt" file and sort out all entries that are not belonging to the current user and then prints the item at index 2 (item no.3) of the remaining entries. This function is called when user inputs "VM" from the menu.
def viewmytasks(username):
    with open("tasks.txt", "r") as taskfile:
        entries = taskfile.readlines()
        entries_list = []
        for i in entries:
            i = i.replace("\n", "")
            i = i.split(", ")
            entries_list.append(i)
        
    count = 1
    userdict = {}
    for index,i in enumerate(entries_list):
        if i[0] == username:
            print(f"{count}: {i[2]}")
            userdict[count] = int(index/2)
            count += 1
            
            
    if count == 1:
        print("No tasks assigned for", username + ".")
        
    
    if True:
        while True:
            try:
                task_choice = int(input("What task do you want to edit? "))
                
                if task_choice == -1:
                    break
                elif 0 < task_choice <= count:
                    usercho = userdict[task_choice]
                    if entries_list[usercho*2][5] == "Yes":
                        print("Unable - You can't edit completed tasks.")
                        continue
                    edit_tasks(usercho)
                    break
                
                else:
                    print("\nInvalid choice. Enter -1 to return to previous menu.")
            except:
                print("\nInvalid choice. Enter -1 to return to previous menu.dd")


# This function (usertask) is for adding new tasks to the "tasks.txt" file. It takes inputs from the user and then asks the user if the entry is correct. If the user accepts it, it will be saved to the file in one line with each input separated with a comma.
def usertask():
    while True:
        username = input("Enter user that is assigned to the task: ")
        title_task = input("Title of the task: ")
        descript_of_the_task = input("Task description: ")

#Changed time part below to fit datetime format, makes the output in "2021-aug-12" format.
        while True:
            try:
                a,b,c = input("Date assigned (ie. 31-12-2021): ").split("-")
            
                if int(c) < 2000:
                    print("insert a valid year with 4 numbers")
                    continue
                assign_date = date(int(c), int(b), int(a))
                assign_date = assign_date.strftime("%d %b %Y")
                break
            except:
                print("make sure to use format dd-mm-yyyy")
        
        
        while True:
            try:
                a,b,c = input("Due date (ie. 31-12-2021): ").split("-")
            
                if int(c) < 2000:
                    print("insert a valid year with 4 numbers")
                    continue
                due_date = date(int(c), int(b), int(a))
                due_date = due_date.strftime("%d %b %Y")
                break
            except:
                print("make sure to use format dd-mm-yyyy")
            
        while True:
            task_complete = input("Task complete? (Yes/No)").capitalize()
        
            if task_complete == "Yes" or task_complete == "No":
                break
            else:
                print("Input Yes or No.")

        correct = input("Confirm the above inputs are correct. (y/n): ").lower()
        if correct != "y":
            print("please enter info again.\n")
        else:
            break
            
    with open("tasks.txt", "r") as readtask:
        existing_tasks_temp = readtask.readlines()
        existing_tasks = []
        
        for i in existing_tasks_temp:
            i = i.split(", ")
            existing_tasks.append(i)


    with open("tasks.txt", "a+") as task:
        try:
            if "\n" not in existing_tasks[-1][5]:
                print("", file=task)
        except:
            pass
        
        print("", file=task)
        print(username + ", " + title_task + ", " + descript_of_the_task + ", " + assign_date + ", " + due_date + ", " + task_complete, file=task)
    

#This function (taskstat) is only provided as an option for the admin-user. This opens both the "user.txt" and "tasks.txt" file and counts the number of entries with the len() method. Then it presents those numbers as number if users and numbers if tasks in the files. This function is called if the user enters "S"

def taskstat():
    with open("tasks.txt", "r") as taskfile:
        entries = taskfile.readlines()
        entries_list = []
        for i in entries:
            i = i.replace("\n", "")
            if i == "":
                continue
            entries_list.append(i)
        no_entries = len(entries_list)
        
            
    with open("user.txt", "r") as userfile:
        users = userfile.readlines()
        no_users = len(users)
    print("\n**** Statistics ****")
    print(f"\nNumber of users: {no_users}.\nNumber of tasks: {no_entries}.\n")
    input("Press enter to continue...")


# New part, make_report function generates task_overview file and user_overview file

def make_reports():
    
    #create task_overview file.
    with open("tasks.txt", "r") as taskfile:
        entries = taskfile.readlines()

        entries_list = []
    
        for i in entries:
            i = i.replace("\n", "")
            if i == "":
                continue
            i = i.split(", ")
            if len(i) < 1:
                continue
            entries_list.append(i)
            
            
    no_tasks = len(entries_list)
    count_completed = 0
    count_incomplete = 0
    count_overdue = 0
    
    for i in entries_list:
        if i[5] == "Yes":
            count_completed += 1
        if i[5] == "No":
            count_incomplete += 1
            duedate = datetime.strptime(i[4], "%d %b %Y").date()
            if duedate < date.today():
                count_overdue += 1
                
        percent_incomp = int((count_incomplete / no_tasks) * 100)
        percent_overdue = int((count_overdue / no_tasks) * 100)
    
    with open("task_overview.txt", "w+") as taskfile:
        print("\t\t*** TASK OVERVIEW ***", file=taskfile)
        print(f"Number of created tasks:\t\t\t\t\t{no_tasks}", file=taskfile)
        print(f"Number of completed tasks:\t\t\t\t{count_completed}", file=taskfile)
        print(f"Number of incompleted tasks:\t\t\t\t{count_incomplete}", file=taskfile)
        print(f"Number of incomplete tasks overdue:\t\t{count_overdue}", file=taskfile)
        print(f"Percentage of tasks incomplete:\t\t\t{percent_incomp}%", file=taskfile)
        print(f"Percentage of incomplete tasks overdue:\t{percent_overdue}%", file=taskfile)
    

    #create user_overview file:
    
    with open("user.txt", "r") as userfile:
        entries = userfile.readlines()

        user_list = []
    
        for i in entries:
            i = i.replace("\n", "")
            if i == "":
                continue
            i = i.split(", ")
            if len(i) < 1:
                continue
            user_list.append(i)
            
            
    no_users = len(user_list)
   
    
    with open("user_overview.txt", "w+") as userfile:
        
        print("\t\t*** USER OVERVIEW ***", file=userfile)
        print(f"Total users in the system:\t\t\t\t{no_users}", file=userfile)
        print(f"Total tasks in the system:\t\t\t\t{no_tasks}", file=userfile)


        for i in user_list:
            usercount = 0
            usercompleted = 0
            userincomplete = 0
            useroverdue = 0
            print("", file=userfile)
            print(f"User report for: {i[0]}", file=userfile)
            
            for j in entries_list:
                if i[0] == j[0]:
                    usercount += 1
                    if j[5] == "Yes":
                        usercompleted += 1
                    if j[5] == "No":
                        userincomplete += 1
                        duedate = datetime.strptime(j[4], "%d %b %Y").date()
                        if duedate < date.today(): 
                            useroverdue += 1
                
                
            if usercount == 0:
                usertotalpercent = "-"
                usertotalcomppercent = "-"
                usertotalincomppercent = "-"
                userincompandoverduepercent = "-"

            else:
                usertotalpercent = int((usercount / no_tasks) * 100)
                usertotalcomppercent = int((usercompleted / usercount) * 100)
                usertotalincomppercent = int((userincomplete / usercount) * 100)
                userincompandoverduepercent = int((useroverdue / usercount) * 100)
        
            print(f"Tasks assigned:\t\t\t\t\t\t{usercount}", file=userfile)
            print(f"Percentage of total tasks:\t\t\t\t{usertotalpercent}%", file=userfile)
            print(f"Percentage of tasks completed:\t\t{usertotalcomppercent}%", file=userfile)
            print(f"Percentage of tasks incompleted:\t\t{usertotalincomppercent}%", file=userfile)
            print(f"Percentage of tasks overdue:\t\t\t{userincompandoverduepercent}%", file=userfile)
    print("\nOverview files created.")
            
            
#Function to print the overview files in the program.

def print_reports():
    make_reports()
    
    with open("task_overview.txt", "r") as tasksfile:
        entries = tasksfile.readlines()
        print()
        for i in entries:
            i = i.replace("\n", "")
            i = i.replace("\t", " ")
            if len(i) < 1:
                continue
            print(i)
        input("Press any key to continue...")
        
    with open("user_overview.txt", "r") as tasksfile:
        entries = tasksfile.readlines()
        print()
        for i in entries:
            i = i.replace("\n", "")
            i = i.replace("\t", " ")

            print(i)
        input("Press any key to continue...")
        
            
#Program starts, this is where thr program structure is controlled.

username = None

print("Welcome to the task manager!\n")

printmenu1(username)
username = menu1selector(username)

print("\nWelcome to the Task Manager", username +"!\n")
while True:
    printmenu1(username)
    print()
    username = menu1selector(username)
