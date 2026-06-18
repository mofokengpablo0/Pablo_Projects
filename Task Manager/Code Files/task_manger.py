# Part1
# ===== Importing external modules ===========
'''This is the section where you will import modules'''

import datetime

# ==== Login Section ====
# TODO: Implement the following functionality
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and passwords from the user.txt file
    - You can use a list or dictionary to store a list of usernames and
       passwords from the file.
    - Use a while loop to validate your user name and password.
'''

# STEP-BY-STEP GUIDANCE:
# 1. Create a data structure (dictionary or list) to store user credentials
# 2. Open and read user.txt file
# 3. Parse each line and extract username and password
# 4. Use a while loop to keep asking for login until credentials are valid
# 5. Once logged in, proceed to the menu
user_credentials = {}
try:
    with open("user.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(", ")
            user_credentials[username] = password
except FileNotFoundError:
    print("Error: user.txt file not found.")
logged_in_user = None
while logged_in_user is None:
    username = input("Enter your username:").strip()
    password = input("Enter your password:").strip()

    if username in user_credentials and user_credentials[username] == password:
        logged_in_user = username
        print(f"Welcome {username}!")
    else:
        print("Invalid username or password. Please try again.")    

while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    menu = input(
        '''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: '''
    ).lower()

    if menu == 'r':
        # TODO: Implement the following functionality
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        
        # STEP-BY-STEP GUIDANCE FOR TASK ONE - REGISTER A NEW USER:
        # STEP 1: Prompt user for a new username
        # STEP 2: Check if username already exists
        # STEP 3: Prompt user for a new password
        # STEP 4: Prompt user to confirm the password
        # STEP 5: Validate that both passwords match
        # STEP 6: If they match - add to dictionary/data structure
        # STEP 7: Write the new user to user.txt file (use append mode)
        # STEP 8: Display success or error message
        new_username = input("Enter a new username: ").strip()
        if new_username in user_credentials:
            print("Username already exists. Please choose a different username.")
        else:
            new_password = input("Enter a new password: ").strip()
            confirm_password = input("Confirm your password: ").strip()
            
            if new_password == confirm_password:
                # Add to dictionary
                user_credentials[new_username] = new_password
                # Write to file
                with open("user.txt", "a") as file:
                    file.write(f"\n{new_username}, {new_password}")
                print("User registered successfully!")
            else:
                print("Passwords do not match. Please try again.")

    elif menu == 'a':
        # TODO: Implement the following functionality
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not
              complete.
        '''
        # Prompt for task details
        assigned_user = input("Enter the username of the person the task is assigned to: ").strip()
        task_title = input("Enter the task title: ").strip()
        task_description = input("Enter the task description: ").strip()
        due_date = input("Enter the due date (DD/MM/YYYY): ").strip()
        
        # Get current date
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        
        # Write to task.txt file (append mode)
        with open("task.txt", "a") as file:
            file.write(f"\n{assigned_user}, {task_title}, {task_description}, {current_date}, {due_date}, No")
        
        print("Task added successfully!")

    elif menu == 'va':
        # TODO: Implement the following functionality
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in
              the PDF
            - It is much easier to read a file using a for loop.'''
        try:
            with open("task.txt", "r") as file:
                for line in file:
                    if line.strip():  # Skip empty lines
                        parts = line.strip().split(", ")
                        if len(parts) == 6:
                            username, title, description, assigned_date, due_date, completed = parts
                            print("Task:\t\t\t" + title)
                            print("Assigned to:\t\t" + username)
                            print("Date assigned:\t\t" + assigned_date)
                            print("Due date:\t\t" + due_date)
                            print("Task complete?\t\t" + completed)
                            print("Task description:\n" + description)
                            print("-" * 50)
        except FileNotFoundError:
            print("No tasks found. The task.txt file does not exist.")

    elif menu == 'vm':
        # TODO: Implement the following functionality
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        try:
            found_tasks = False
            with open("task.txt", "r") as file:
                for line in file:
                    if line.strip():  # Skip empty lines
                        parts = line.strip().split(", ")
                        if len(parts) == 6:
                            username, title, description, assigned_date, due_date, completed = parts
                            if username == logged_in_user:
                                print("Task:\t\t\t" + title)
                                print("Assigned to:\t\t" + username)
                                print("Date assigned:\t\t" + assigned_date)
                                print("Due date:\t\t" + due_date)
                                print("Task complete?\t\t" + completed)
                                print("Task description:\n" + description)
                                print("-" * 50)
                                found_tasks = True
            
            if not found_tasks:
                print("No tasks assigned to you.")
        except FileNotFoundError:
            print("No tasks found. The task.txt file does not exist.")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")


#my user and task text files are empty, so I will not be able to test the code until maybe if i have permision to populate those files with some data. I have implemented the code for all the menu options, but I cannot test it without data in the user.txt and task.txt files.        