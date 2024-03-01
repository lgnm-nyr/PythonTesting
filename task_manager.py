# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)
    
#====Function Defining======================

''' Functions for main loop '''

# Function for registering new user
def reg_user():
   
    # Input new username
    print('=' * 50)
    new_username = input("\nNew Username: ")
    while new_username in username_password.keys():
        print("\nThis username already exists, please enter a new one!")
        new_username = input("New Username: ")

    # Input of a new password
    new_password = input("New Password: ")

    # Password Confirmation
    confirm_password = input("Confirm Password: ")
    print('=' * 50)
    
    # Password validation
    if new_password == confirm_password:
        # If they are the same, add them to the user.txt file,
        print("\nNew user added\n")
        print('=' * 50)
        username_password[new_username] = new_password
        
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # Otherwise error msg + retry
    else:
        print("Passwords do not match, please restart adding a new user")
        reg_user()
   

# Funtion for adding new task
def add_task():

    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.
    '''
    print('=' * 50)
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        add_task() #Changed here to make sense
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Enter due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    
    # Setup task and add to file
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write) + "\n")
    print("Task successfully added.\n")
    print('=' * 50)
 
 
# Function to view all tasks
def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling) 
    '''

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print('=' * 50)
        print(disp_str)
        print('=' * 50)
        
         
# Function to view and edit user's tasks
def view_mine():
    
    # Show Tasks assigned to current user
    for i, t in enumerate(task_list):
        if t['username'] == curr_user:
            disp_str = f"\n{i+1}. Task: \t\t {t['title']}\n"\
                        f"    Assigned to: \t {t['username']}\n"\
                        f"    Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"\
                        f"    Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"\
                        f"    Task Description: \n {t['description']}\n"
            print('=' * 50)
            print(disp_str)
            print('=' * 50)
        
    # Option input
    task_num = input("\nEnter the number of the task to edit or -1 to return to the main menu: ")
    print('=' * 50)
    
    # Data validation
    while not task_num.isdigit() and task_num != "-1":
        print("Invalid input. Please enter a number or -1 to return to the main menu.")
        task_num = input("\nEnter the number of the task to edit or -1 to return to the main menu: ")
        print('=' * 50)
    
    
    # go to main menu
    if task_num == "-1":
    
        return
    
    # Task choice
    else:
        # Choosing Task
        task_num = int(task_num) - 1
        if task_num < 0 or task_num >= len(task_list):
            print("Invalid task number, please try again.")
            view_mine()
            
        # Selected Task
        task = task_list[task_num]
        
        # Completion Check
        if task['completed']:
            print("This task has already been completed and cannot be edited.")
            view_mine()
        
        # Options to edit tasks
        else:
            print("Select an option to edit the task:")
            print("1. Mark as complete")
            print("2. Edit username")
            print("3. Edit due date")
            print('=' * 50)
            option = input("Enter the number of the option: ")
            
            # Task completion
            if option == "1":
                task['completed'] = True
                print("\nTask marked as complete.\n")
                print('=' * 50)
                
            # Change user
            elif option == "2":
                new_username = input("Enter the new username: ")
                # making sure new user exists
                while new_username not in username_password.keys():
                    print("User does not exist. Please enter a valid username")
                    new_username = input("Enter the new username: ")
                task['username'] = new_username
                print("Username successfully changed.")
                print('=' * 50)
                
            # Change due date
            elif option == "3":
                # Correct date time inputs
                while True:
                    try:
                        new_due_date = input("New due date of task (YYYY-MM-DD): ")
                        due_date_time = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                        task['due_date'] = due_date_time
                        print("Due date successfully changed.\n")
                        print('=' * 50)
                        break
                    except ValueError:
                        print("Invalid datetime format. Please use the format specified.\n")
                        print('=' * 50)
            
            # If other option selected go to main menu
            else:
                print("Invalid option, please try again.")
                print('=' * 50)
                view_mine()
        
        # Updating files
        with open("tasks.txt", "w+") as f:
            for i, t in enumerate(task_list):
                if i == task_num:
                    changed_task = [
                        t['username'],
                        t['title'],
                        t['description'],
                        t['due_date'].strftime(DATETIME_STRING_FORMAT),
                        t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if t['completed'] else "No"
                    ]
                else:
                    changed_task = [
                        t['username'],
                        t['title'],
                        t['description'],
                        t['due_date'].strftime(DATETIME_STRING_FORMAT),
                        t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if t['completed'] else "No"
                    ]
                f.write(";".join(changed_task) + "\n")


# Calling both task & user reports
def reports():
    generate_task_overview()
    generate_user_overview()

# Function to generate task statistics
def generate_task_overview():    
    num_tasks = len(task_list)
    num_completed_tasks =sum([task['completed'] for task in task_list])
    num_uncompleted_tasks = num_tasks - num_completed_tasks
    num_overdue_tasks = sum([not task['completed'] and task['due_date'] < datetime.today() for task in task_list])

    # Writing/editing new file with info
    with open("task_overview.txt", "w") as f:
        f.write(f"Total number of tasks: {num_tasks}\n")
        f.write(f"Total number of completed tasks: {num_completed_tasks}\n")
        f.write(f"Total number of uncompleted tasks: {num_uncompleted_tasks}\n")
        f.write(f"Total number of overdue tasks: {num_overdue_tasks}\n")
        f.write(f"Percentage of tasks that are incomplete: {num_uncompleted_tasks/num_tasks*100:.2f}%\n")
        f.write(f"Percentage of tasks that are overdue: {num_overdue_tasks/num_tasks*100:.2f}%\n")

# Function to generate user statistics
def generate_user_overview():
    num_users = len(username_password.keys())
    num_tasks = len(task_list)

    user_stats = {}
    # Getting each user's total tasks
    for user in username_password.keys():
        num_user_tasks = sum([task['username'] == user for task in task_list])
        num_user_completed_tasks = sum([task['username'] == user and task['completed'] for task in task_list])
        num_user_uncompleted_tasks = num_user_tasks - num_user_completed_tasks
        num_user_overdue_tasks = sum([task['username'] == user and not task['completed'] and task['due_date'] < datetime.today() for task in task_list])

        # Recording each user's stats, if they have 0 tasks, change num to 0 so error not produced
        user_stats[user] = {
            'total_tasks': num_user_tasks,
            'completed_tasks_percentage': num_user_completed_tasks/num_user_tasks*100 if num_user_tasks != 0 else 0,
            'uncompleted_tasks_percentage': num_user_uncompleted_tasks/num_user_tasks*100 if num_user_tasks != 0 else 0,
            'overdue_tasks_percentage': num_user_overdue_tasks/num_user_tasks*100 if num_user_tasks != 0 else 0
        }

    # Write file for user statistics report
    with open("user_overview.txt", "w") as f:
        f.write(f"Total number of users: {num_users}\n")
        f.write(f"Total number of tasks: {num_tasks}\n")
        for user, stats in user_stats.items():
            f.write(f"\nUser: {user}\n")
            f.write(f"Total number of tasks assigned: {stats['total_tasks']}\n")
            f.write(f"Percentage of total tasks assigned: {stats['total_tasks']/num_tasks*100:.2f}%\n")
            f.write(f"Percentage of tasks completed: {stats['completed_tasks_percentage']:.2f}%\n")
            f.write(f"Percentage of tasks not completed: {stats['uncompleted_tasks_percentage']:.2f}%\n")
            f.write(f"Percentage of tasks overdue: {stats['overdue_tasks_percentage']:.2f}%\n")


# Generating statistics for reading on screen
def display_statistics(): 
    
    '''Instructions said to generate stats based on files tasks.txt and user.txt
    when I could use the previous functions and code (reports() and task_list) instead and use those to present.
    I've left as is to keep in line with instructions but unsure if this is the most optimal here.
    '''
    
    # In case files don't exist
    if not os.path.exists("tasks.txt") or not os.path.exists("user.txt"): 
        reports()
        
    # Read data from files
    with open("tasks.txt", "r") as task_file, open("user.txt", "r") as user_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]
        user_data = user_file.read().split("\n")

    num_tasks = len(task_data)
    num_users = len(user_data)
    print(task_data)

    # Calculate statistics
    num_completed_tasks = sum([task.split(';')[-1] == "Yes" for task in task_data])
    print(task.strip('').split(';')[-1] for task in task_data)
    num_uncompleted_tasks = num_tasks - num_completed_tasks
    num_overdue_tasks = sum([datetime.strptime(task.split(';')[-3], DATETIME_STRING_FORMAT) < datetime.today() and task.split(';')[-1] == "No" for task in task_data])

    # Get and calculate user stats
    user_stats = {}
    for user in user_data:
        username, password = user.strip().split(";")
        user_stats[username] = {"total_tasks": sum([task.split(';')[0] == username for task in task_data]),
                                "completed_tasks": sum([task.split(';')[0] == username and task.split(';')[-1] == "Yes" for task in task_data]),
                                "uncompleted_tasks": sum([task.split(';')[0] == username and task.split(';')[-1] == "No" for task in task_data]),
                                "overdue_tasks": sum([task.split(';')[0] == username and datetime.strptime(task.split(';')[-3], DATETIME_STRING_FORMAT) < datetime.today() for task in task_data])}

    # Display statistics
    print("\nStatistics:")
    print(f"Number of tasks: {num_tasks}")
    print(f"Number of users: {num_users}")
    print(f"Number of completed tasks: {num_completed_tasks}")
    print(f"Number of uncompleted tasks: {num_uncompleted_tasks}")
    print(f"Number of overdue tasks: {num_overdue_tasks}")
    print("\nUser statistics:")
    for user, stats in user_stats.items():
        print(f"\nUser: {user}")
        print(f"Total tasks: {stats['total_tasks']}")
        print(f"Completed tasks: {stats['completed_tasks']}")
        print(f"Uncompleted tasks: {stats['uncompleted_tasks']}")
        print(f"Overdue tasks: {stats['overdue_tasks']}")

    
#====End of Function Definitions==========================

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print('=' * 50)
    print("\nLOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password\n")
        continue
    else:
        print("Login Successful!\n")
        print('=' * 50)
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print('=' * 50)
    print()
    menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate reports
    ds - Display statistics
    e - Exit
    : ''').lower()

    # Option to register a user
    if menu == 'r':
        reg_user()

    # Option to add a task
    elif menu == 'a':
        add_task()

    # Option to view all tasks
    elif menu == 'va':
        view_all()

    # Option to view "my" tasks
    elif menu == 'vm':
        view_mine()
    
    # Option to generate reports   
    elif menu == 'gr':
        reports()
                
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        display_statistics()   

    # Option to exit program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # When misinput
    else:
        print("You have made a wrong choice, Please Try again")
        