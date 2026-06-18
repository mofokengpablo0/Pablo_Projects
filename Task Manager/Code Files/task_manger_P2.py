#Part2
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
    with open("Level 1 - Python for Software Engineering\\M03T10 – Capstone Project – Task Manager\\Code Files\\user.txt", "r") as file:
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
r - register user
a - add task
va - view all tasks
vm - view my tasks
vc - view completed tasks
del - delete a task
ds - display statistics
gr - generate reports
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
                with open("Level 1 - Python for Software Engineering\\M03T10 – Capstone Project – Task Manager\\Code Files\\user.txt", "a") as file:
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
        with open("tasks.txt", "a") as file:
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
            with open("tasks.txt", "r") as file:
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
        # View my tasks
        try:
            tasks = []
            with open("Code Files/tasks.txt", "r") as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split(", ")
                        if len(parts) == 6:
                            username, title, description, assigned_date, due_date, completed = parts
                            if username == logged_in_user:
                                tasks.append((username, title, description, assigned_date, due_date, completed))
            
            if not tasks:
                print("No tasks assigned to you.")
            else:
                print("Your tasks:")
                for i, (username, title, description, assigned_date, due_date, completed) in enumerate(tasks, 1):
                    print(f"{i}. {title} - Due: {due_date} - Completed: {completed}")
                
                def get_valid_task_number():
                    try:
                        task_num = input("Enter the number of the task you want to mark as complete (or -1 to return to menu): ").strip()
                        if task_num == "-1":
                            return -1
                        task_num = int(task_num)
                        if 1 <= task_num <= len(tasks):
                            return task_num
                        else:
                            print("Invalid task number. Please try again.")
                            return get_valid_task_number()
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        return get_valid_task_number()
                
                task_num = get_valid_task_number()
                if task_num != -1:
                    # Mark as complete
                    tasks[task_num - 1] = (tasks[task_num - 1][0], tasks[task_num - 1][1], tasks[task_num - 1][2], tasks[task_num - 1][3], tasks[task_num - 1][4], "Yes")
                    # Rewrite all tasks
                    all_tasks = []
                    with open("Code Files/tasks.txt", "r") as file:
                        for line in file:
                            if line.strip():
                                parts = line.strip().split(", ")
                                if len(parts) == 6:
                                    all_tasks.append(list(parts))
                    
                    # Update the specific task
                    task_index = 0
                    for i, t in enumerate(all_tasks):
                        if t[0] == logged_in_user:
                            if task_index == task_num - 1:
                                all_tasks[i][5] = "Yes"
                                break
                            task_index += 1
                    
                    with open("Code Files/tasks.txt", "w") as file:
                        for t in all_tasks:
                            file.write(", ".join(t) + "\n")
                    
                    print("Task marked as complete!")
        except FileNotFoundError:
            print("No tasks found. The tasks.txt file does not exist.")

    elif menu == 'vc':
        # View completed tasks
        try:
            with open("Code Files/tasks.txt", "r") as file:
                found_completed = False
                for line in file:
                    if line.strip():  # Skip empty lines
                        parts = line.strip().split(", ")
                        if len(parts) == 6:
                            username, title, description, assigned_date, due_date, completed = parts
                            if completed.lower() == 'yes':
                                print("Task:\t\t\t" + title)
                                print("Assigned to:\t\t" + username)
                                print("Date assigned:\t\t" + assigned_date)
                                print("Due date:\t\t" + due_date)
                                print("Task complete?\t\t" + completed)
                                print("Task description:\n" + description)
                                print("-" * 50)
                                found_completed = True
                if not found_completed:
                    print("No completed tasks found.")
        except FileNotFoundError:
            print("No tasks found. The tasks.txt file does not exist.")

    elif menu == 'del':
        # Delete a task
        try:
            tasks = []
            with open("Code Files/tasks.txt", "r") as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split(", ")
                        if len(parts) == 6:
                            username, title, description, assigned_date, due_date, completed = parts
                            if username == logged_in_user:
                                tasks.append((username, title, description, assigned_date, due_date, completed))
            
            if not tasks:
                print("No tasks assigned to you to delete.")
            else:
                print("Your tasks:")
                for i, (username, title, description, assigned_date, due_date, completed) in enumerate(tasks, 1):
                    print(f"{i}. {title} - Due: {due_date} - Completed: {completed}")
                
                try:
                    task_num = int(input("Enter the number of the task to delete: ").strip())
                    if 1 <= task_num <= len(tasks):
                        # Remove the task
                        del tasks[task_num - 1]
                        # Rewrite the file with remaining tasks
                        with open("Code Files/tasks.txt", "w") as file:
                            for task in tasks:
                                file.write(f"{task[0]}, {task[1]}, {task[2]}, {task[3]}, {task[4]}, {task[5]}\n")
                        print("Task deleted successfully!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        except FileNotFoundError:
            print("No tasks found. The tasks.txt file does not exist.")

    elif menu == 'gr':
        # Generate reports
        try:
            # Read tasks
            tasks = []
            with open("Code Files/tasks.txt", "r") as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split(", ")
                        if len(parts) == 6:
                            username, title, description, assigned_date, due_date, completed = parts
                            tasks.append((username, title, description, assigned_date, due_date, completed))
            
            # Read users
            users = list(user_credentials.keys())
            
            current_date = datetime.datetime.now().date()
            
            # Helper to parse date
            def parse_date(date_str):
                return datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            
            # Calculate for task_overview
            total_tasks = len(tasks)
            completed_tasks = sum(1 for t in tasks if t[5].lower() == 'yes')
            uncompleted_tasks = total_tasks - completed_tasks # run through loops and cater for corrupted tasks (shortcut taken by not catering for corrupted files)
            overdue_tasks = sum(1 for t in tasks if t[5].lower() == 'no' and parse_date(t[4]) < current_date) #debugging note print all prevv to check
            perc_incomplete = (uncompleted_tasks / total_tasks * 100) if total_tasks > 0 else 0
            perc_overdue = (overdue_tasks / total_tasks * 100) if total_tasks > 0 else 0
            
            # Write task_overview.txt
            with open("task_overview.txt", "w") as file:
                file.write(f"Total tasks: {total_tasks}\n")
                file.write(f"Completed tasks: {completed_tasks}\n")
                file.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
                file.write(f"Overdue tasks: {overdue_tasks}\n")
                file.write(f"Percentage incomplete: {perc_incomplete:.2f}%\n")
                file.write(f"Percentage overdue: {perc_overdue:.2f}%\n")
            
            # Calculate for user_overview
            total_users = len(users)
            
            with open("user_overview.txt", "w") as file:
                file.write(f"Total users: {total_users}\n")
                file.write(f"Total tasks: {total_tasks}\n")
                for user in users:
                    user_tasks = [t for t in tasks if t[0] == user]
                    total_assigned = len(user_tasks)
                    perc_assigned = (total_assigned / total_tasks * 100) if total_tasks > 0 else 0
                    completed_assigned = sum(1 for t in user_tasks if t[5].lower() == 'yes')
                    perc_completed = (completed_assigned / total_assigned * 100) if total_assigned > 0 else 0
                    perc_to_complete = ((total_assigned - completed_assigned) / total_assigned * 100) if total_assigned > 0 else 0
                    overdue_assigned = sum(1 for t in user_tasks if t[5].lower() == 'no' and parse_date(t[4]) < current_date)
                    perc_overdue_user = (overdue_assigned / total_assigned * 100) if total_assigned > 0 else 0
                    
                    file.write(f"\nUser: {user}\n")
                    file.write(f"Total tasks assigned: {total_assigned}\n")
                    file.write(f"Percentage of total tasks: {perc_assigned:.2f}%\n")
                    file.write(f"Percentage completed: {perc_completed:.2f}%\n")
                    file.write(f"Percentage to complete: {perc_to_complete:.2f}%\n")
                    file.write(f"Percentage overdue: {perc_overdue_user:.2f}%\n")
            
            print("Reports generated successfully!")
        except FileNotFoundError:
            print("Error generating reports. Files not found.")

    elif menu == 'ds':
        # Display statistics
        import os
        if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
            print("Reports not found. Generating reports first...")
            # Copy the generate code here or call it, but since it's inline, repeat
            try:
                # Read tasks
                tasks = []
                with open("Code Files/tasks.txt", "r") as file:
                    for line in file:
                        if line.strip():
                            parts = line.strip().split(", ")
                            if len(parts) == 6:
                                username, title, description, assigned_date, due_date, completed = parts
                                tasks.append((username, title, description, assigned_date, due_date, completed))
                
                # Read users
                users = list(user_credentials.keys())
                
                current_date = datetime.datetime.now().date()
                
                # Helper to parse date
                def parse_date(date_str):
                    return datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
                
                # Calculate for task_overview
                total_tasks = len(tasks)
                completed_tasks = sum(1 for t in tasks if t[5].lower() == 'yes')
                uncompleted_tasks = total_tasks - completed_tasks
                overdue_tasks = sum(1 for t in tasks if t[5].lower() == 'no' and parse_date(t[4]) < current_date)
                perc_incomplete = (uncompleted_tasks / total_tasks * 100) if total_tasks > 0 else 0
                perc_overdue = (overdue_tasks / total_tasks * 100) if total_tasks > 0 else 0
                
                # Write task_overview.txt
                with open("task_overview.txt", "w") as file:
                    file.write(f"Total tasks: {total_tasks}\n")
                    file.write(f"Completed tasks: {completed_tasks}\n")
                    file.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
                    file.write(f"Overdue tasks: {overdue_tasks}\n")
                    file.write(f"Percentage incomplete: {perc_incomplete:.2f}%\n")
                    file.write(f"Percentage overdue: {perc_overdue:.2f}%\n")
                
                # Calculate for user_overview
                total_users = len(users)
                
                with open("user_overview.txt", "w") as file:
                    file.write(f"Total users: {total_users}\n")
                    file.write(f"Total tasks: {total_tasks}\n")
                    for user in users:
                        user_tasks = [t for t in tasks if t[0] == user]
                        total_assigned = len(user_tasks)
                        perc_assigned = (total_assigned / total_tasks * 100) if total_tasks > 0 else 0
                        completed_assigned = sum(1 for t in user_tasks if t[5].lower() == 'yes')
                        perc_completed = (completed_assigned / total_assigned * 100) if total_assigned > 0 else 0
                        perc_to_complete = ((total_assigned - completed_assigned) / total_assigned * 100) if total_assigned > 0 else 0
                        overdue_assigned = sum(1 for t in user_tasks if t[5].lower() == 'no' and parse_date(t[4]) < current_date)
                        perc_overdue_user = (overdue_assigned / total_assigned * 100) if total_assigned > 0 else 0
                        
                        file.write(f"\nUser: {user}\n")
                        file.write(f"Total tasks assigned: {total_assigned}\n")
                        file.write(f"Percentage of total tasks: {perc_assigned:.2f}%\n")
                        file.write(f"Percentage completed: {perc_completed:.2f}%\n")
                        file.write(f"Percentage to complete: {perc_to_complete:.2f}%\n")
                        file.write(f"Percentage overdue: {perc_overdue_user:.2f}%\n")
                
                print("Reports generated.")
            except FileNotFoundError:
                print("Error generating reports. Files not found.")
        
        # Now display
        print("\n--- TASK OVERVIEW ---")
        try:
            with open("task_overview.txt", "r") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("Task overview file not found.")
        
        print("\n--- USER OVERVIEW ---")
        try:
            with open("user_overview.txt", "r") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("User overview file not found.")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")


#my user and task text files are empty, so I will not be able to test the code until maybe if i have permision to populate those files with some data. I have implemented the code for all the menu options, but I cannot test it without data in the user.txt and task.txt files.        