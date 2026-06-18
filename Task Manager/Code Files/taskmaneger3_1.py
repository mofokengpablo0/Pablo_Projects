# task_manager.py
# Task Manager Application - Capstone Project
# A program for managing tasks assigned to team members

import os
from datetime import datetime

# File paths
USER_FILE = "Level 1 - Python for Software Engineering\\M03T10 – Capstone Project – Task Manager\\Code Files\\user.txt"
TASKS_FILE = "Level 1 - Python for Software Engineering\\M03T10 – Capstone Project – Task Manager\\Code Files\\tasks.txt"
TASK_OVERVIEW_FILE = "Level 1 - Python for Software Engineering\\M03T10 – Capstone Project – Task Manager\\Code Files\\task_overview.txt"
USER_OVERVIEW_FILE = "Level 1 - Python for Software Engineering\\M03T10 – Capstone Project – Task Manager\\Code Files\\user_overview.txt"

# Date format for display
DATE_FORMAT = "%d %b %Y"


def read_users():
    """
    Read users from user.txt file.
    Returns a dictionary of {username: password}.
    """
    users = {}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    # Handle possible comma-space or just comma separation
                    if ', ' in line:
                        username, password = line.split(', ', 1)
                    else:
                        username, password = line.split(',', 1)
                        password = password.strip()
                    users[username.strip()] = password.strip()
    return users


def write_user(username, password):
    """
    Write a new user to user.txt file.
    """
    with open(USER_FILE, 'a') as file:
        file.write(f"{username}, {password}\n")


def read_tasks():
    """
    Read tasks from tasks.txt file.
    Returns a list of dictionaries, each representing a task.
    """
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(', ')
                    if len(parts) >= 6:
                        task = {
                            "assigned_to": parts[0],
                            "title": parts[1],
                            "description": parts[2],
                            "date_assigned": parts[3],
                            "due_date": parts[4],
                            "completed": parts[5]
                        }
                        tasks.append(task)
    return tasks


def write_task(task):
    """
    Write a single task to tasks.txt file.
    """
    with open(TASKS_FILE, 'a') as file:
        file.write(f"{task['assigned_to']}, {task['title']}, "
                   f"{task['description']}, {task['date_assigned']}, "
                   f"{task['due_date']}, {task['completed']}\n")


def update_tasks_file(tasks):
    """
    Overwrite tasks.txt with the current list of tasks.
    """
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task['assigned_to']}, {task['title']}, "
                       f"{task['description']}, {task['date_assigned']}, "
                       f"{task['due_date']}, {task['completed']}\n")


def login():
    """
    Handle user login authentication.
    Returns the logged-in username.
    """
    users = read_users()
    
    while True:
        print("\n" + "=" * 50)
        print("          TASK MANAGER LOGIN")
        print("=" * 50)
        
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        
        if username in users and users[username] == password:
            print(f"\n✓ Login successful! Welcome, {username}!")
            return username
        else:
            print("\n✗ Invalid username or password. Please try again.")


def reg_user(current_user, users):
    """
    Register a new user. Only admin can perform this action.
    Checks for duplicate usernames.
    """
    if current_user != "admin":
        print("\n✗ Access denied. Only admin can register new users.")
        return users
    
    print("\n" + "-" * 40)
    print("         REGISTER NEW USER")
    print("-" * 40)
    
    while True:
        new_username = input("Enter new username: ").strip()
        
        # Check for duplicate username
        if new_username in users:
            print(f"✗ Username '{new_username}' already exists. Please choose a different username.")
            continue
        
        new_password = input("Enter password: ").strip()
        confirm_password = input("Confirm password: ").strip()
        
        if new_password == confirm_password:
            write_user(new_username, new_password)
            users[new_username] = new_password
            print(f"\n✓ User '{new_username}' registered successfully!")
            return users
        else:
            print("\n✗ Passwords do not match. Please try again.")


def add_task():
    """
    Add a new task to the system.
    """
    users = read_users()
    
    print("\n" + "-" * 40)
    print("           ADD NEW TASK")
    print("-" * 40)
    
    # Get assigned user
    while True:
        assigned_to = input("Enter username of assigned person: ").strip()
        if assigned_to == "":
            print("✗ Username cannot be empty. Please try again.")
            continue
        if assigned_to in users:
            break
        print(f"✗ User '{assigned_to}' not found. Please enter a valid username.")
    
    title = input("Enter task title: ").strip()
    while title == "":
        title = input("Task title cannot be empty. Enter task title: ").strip()
    
    description = input("Enter task description: ").strip()
    while description == "":
        description = input("Task description cannot be empty. Enter task description: ").strip()
    
    due_date = input("Enter due date (DD MMM YYYY, e.g., 25 Dec 2024): ").strip()
    while due_date == "":
        due_date = input("Due date cannot be empty. Enter due date: ").strip()
    
    # Get current date
    current_date = datetime.now().strftime(DATE_FORMAT)
    
    new_task = {
        "assigned_to": assigned_to,
        "title": title,
        "description": description,
        "date_assigned": current_date,
        "due_date": due_date,
        "completed": "No"
    }
    
    write_task(new_task)
    print("\n✓ Task added successfully!")


def format_task_display(task, task_number=None):
    """
    Format a single task for display.
    Returns a formatted string.
    """
    prefix = f"\nTask {task_number}:" if task_number else "\n"
    
    return (f"{prefix}\n"
            f"╔{'═' * 55}╗\n"
            f"║ Task:          {task['title']:<39}║\n"
            f"║ Assigned to:   {task['assigned_to']:<39}║\n"
            f"║ Date assigned: {task['date_assigned']:<39}║\n"
            f"║ Due date:      {task['due_date']:<39}║\n"
            f"║ Completed:     {task['completed']:<39}║\n"
            f"║ Description:   {task['description']:<39}║\n"
            f"╚{'═' * 55}╝")


def view_all():
    """
    Display all tasks in an easy-to-read format.
    """
    tasks = read_tasks()
    
    if not tasks:
        print("\n✗ No tasks found.")
        return
    
    print("\n" + "=" * 60)
    print("               ALL TASKS")
    print("=" * 60)
    
    for i, task in enumerate(tasks, 1):
        print(format_task_display(task, i))


def get_valid_task_number(tasks, current_user):
    """
    Recursive function to get a valid task number from the user.
    Returns the selected task index (0-based) or -1 to exit.
    """
    # Filter tasks for current user
    user_tasks = [i for i, task in enumerate(tasks) if task['assigned_to'] == current_user]
    
    try:
        choice = input("\nEnter task number to view/edit (-1 to return to menu): ").strip()
        
        # Base case: user wants to exit
        if choice == "-1":
            return -1
        
        task_num = int(choice)
        
        if 1 <= task_num <= len(user_tasks):
            return user_tasks[task_num - 1]
        else:
            print(f"✗ Invalid task number. Please enter a number between 1 and {len(user_tasks)}.")
            return get_valid_task_number(tasks, current_user)
    
    except ValueError:
        print("✗ Invalid input. Please enter a valid number or -1.")
        return get_valid_task_number(tasks, current_user)


def view_mine(current_user):
    """
    Display tasks assigned to the current user and allow editing.
    """
    tasks = read_tasks()
    
    if not tasks:
        print(f"\n✗ No tasks found.")
        return
    
    # Filter tasks for current user
    user_tasks = [task for task in tasks if task['assigned_to'] == current_user]
    
    if not user_tasks:
        print(f"\n✗ No tasks assigned to {current_user}.")
        return
    
    print("\n" + "=" * 60)
    print(f"        TASKS ASSIGNED TO {current_user.upper()}")
    print("=" * 60)
    
    for i, task in enumerate(user_tasks, 1):
        print(format_task_display(task, i))
    
    # Get valid task selection using recursive function
    task_index = get_valid_task_number(tasks, current_user)
    
    if task_index == -1:
        return
    
    selected_task = tasks[task_index]
    
    # Check if task is already completed
    if selected_task['completed'] == "Yes":
        print("\n✗ This task is already completed and cannot be edited.")
        return
    
    print("\n" + "-" * 35)
    print("What would you like to do?")
    print("1. Mark task as complete")
    print("2. Edit task")
    print("-" * 35)
    
    action = input("Enter your choice (1 or 2): ").strip()
    
    if action == "1":
        selected_task['completed'] = "Yes"
        update_tasks_file(tasks)
        print("\n✓ Task marked as complete!")
    
    elif action == "2":
        print("\nWhat would you like to edit?")
        print("1. Assign to different user")
        print("2. Change due date")
        print("3. Both")
        edit_choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        if edit_choice in ["1", "3"]:
            new_user = input("Enter new assigned username: ").strip()
            users = read_users()
            if new_user in users:
                selected_task['assigned_to'] = new_user
                print("✓ Assigned user updated.")
            else:
                print("✗ User not found. Assigned user not changed.")
        
        if edit_choice in ["2", "3"]:
            new_due_date = input("Enter new due date (DD MMM YYYY): ").strip()
            selected_task['due_date'] = new_due_date
            print("✓ Due date updated.")
        
        update_tasks_file(tasks)
        print("\n✓ Task updated successfully!")
    
    else:
        print("✗ Invalid choice.")


def view_completed():
    """
    Display all completed tasks (admin only).
    """
    tasks = read_tasks()
    completed_tasks = [task for task in tasks if task['completed'] == "Yes"]
    
    if not completed_tasks:
        print("\n✗ No completed tasks found.")
        return
    
    print("\n" + "=" * 60)
    print("           COMPLETED TASKS")
    print("=" * 60)
    
    for i, task in enumerate(completed_tasks, 1):
        print(format_task_display(task, i))


def delete_task():
    """
    Delete a specific task (admin only).
    """
    tasks = read_tasks()
    
    if not tasks:
        print("\n✗ No tasks to delete.")
        return
    
    print("\n" + "=" * 60)
    print("             DELETE TASK")
    print("=" * 60)
    
    for i, task in enumerate(tasks, 1):
        print(format_task_display(task, i))
    
    try:
        task_num = int(input("\nEnter task number to delete (-1 to cancel): ").strip())
        
        if task_num == -1:
            return
        
        if 1 <= task_num <= len(tasks):
            confirm = input(f"Are you sure you want to delete '{tasks[task_num - 1]['title']}'? (y/n): ").strip().lower()
            if confirm == 'y':
                deleted_task = tasks.pop(task_num - 1)
                update_tasks_file(tasks)
                print(f"\n✓ Task '{deleted_task['title']}' deleted successfully!")
            else:
                print("Delete cancelled.")
        else:
            print("✗ Invalid task number.")
    except ValueError:
        print("✗ Invalid input.")


def generate_reports():
    """
    Generate task_overview.txt and user_overview.txt files.
    """
    tasks = read_tasks()
    users = read_users()
    
    # Task overview calculations
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'] == "Yes")
    uncompleted_tasks = total_tasks - completed_tasks
    
    # Calculate overdue tasks (uncompleted and passed due date)
    current_date = datetime.now()
    overdue_tasks = 0
    
    for task in tasks:
        if task['completed'] == "No":
            try:
                due_date = datetime.strptime(task['due_date'], DATE_FORMAT)
                if due_date < current_date:
                    overdue_tasks += 1
            except ValueError:
                # If date parsing fails, skip this task for overdue calculation
                pass
    
    incomplete_percent = (uncompleted_tasks / total_tasks * 100) if total_tasks > 0 else 0
    overdue_percent = (overdue_tasks / total_tasks * 100) if total_tasks > 0 else 0
    
    # Write task_overview.txt
    with open(TASK_OVERVIEW_FILE, 'w') as file:
        file.write("=" * 50 + "\n")
        file.write("           TASK OVERVIEW REPORT\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"Total number of tasks:                 {total_tasks}\n")
        file.write(f"Total number of completed tasks:       {completed_tasks}\n")
        file.write(f"Total number of uncompleted tasks:     {uncompleted_tasks}\n")
        file.write(f"Total number of overdue tasks:         {overdue_tasks}\n")
        file.write(f"Percentage of incomplete tasks:        {incomplete_percent:.1f}%\n")
        file.write(f"Percentage of overdue tasks:           {overdue_percent:.1f}%\n")
    
    # User overview calculations
    total_users = len(users)
    
    with open(USER_OVERVIEW_FILE, 'w') as file:
        file.write("=" * 50 + "\n")
        file.write("           USER OVERVIEW REPORT\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"Total number of users:    {total_users}\n")
        file.write(f"Total number of tasks:    {total_tasks}\n\n")
        file.write("-" * 40 + "\n")
        
        for username in users:
            user_tasks = [task for task in tasks if task['assigned_to'] == username]
            user_task_count = len(user_tasks)
            
            # Calculate percentages
            percent_of_total = (user_task_count / total_tasks * 100) if total_tasks > 0 else 0
            
            user_completed = sum(1 for task in user_tasks if task['completed'] == "Yes")
            user_uncompleted = user_task_count - user_completed
            percent_completed = (user_completed / user_task_count * 100) if user_task_count > 0 else 0
            percent_uncompleted = (user_uncompleted / user_task_count * 100) if user_task_count > 0 else 0
            
            # Count overdue tasks for this user
            user_overdue = 0
            current_date = datetime.now()
            for task in user_tasks:
                if task['completed'] == "No":
                    try:
                        due_date = datetime.strptime(task['due_date'], DATE_FORMAT)
                        if due_date < current_date:
                            user_overdue += 1
                    except ValueError:
                        pass
            
            percent_overdue = (user_overdue / user_task_count * 100) if user_task_count > 0 else 0
            
            file.write(f"\n📌 User: {username}\n")
            file.write(f"   ├─ Tasks assigned:           {user_task_count}\n")
            file.write(f"   ├─ % of total tasks:         {percent_of_total:.1f}%\n")
            file.write(f"   ├─ % completed:              {percent_completed:.1f}%\n")
            file.write(f"   ├─ % incomplete:             {percent_uncompleted:.1f}%\n")
            file.write(f"   └─ % incomplete & overdue:   {percent_overdue:.1f}%\n")
    
    print("\n✓ Reports generated successfully!")
    print(f"  - {TASK_OVERVIEW_FILE}")
    print(f"  - {USER_OVERVIEW_FILE}")


def display_statistics():
    """
    Display statistics from the overview reports.
    Generate reports if they don't exist.
    """
    # Generate reports if they don't exist
    if not os.path.exists(TASK_OVERVIEW_FILE) or not os.path.exists(USER_OVERVIEW_FILE):
        print("\n📊 Reports not found. Generating them now...")
        generate_reports()
    
    print("\n" + "=" * 60)
    print("                 SYSTEM STATISTICS")
    print("=" * 60)
    
    # Display task overview
    if os.path.exists(TASK_OVERVIEW_FILE):
        with open(TASK_OVERVIEW_FILE, 'r') as file:
            print(file.read())
    
    # Display user overview
    if os.path.exists(USER_OVERVIEW_FILE):
        with open(USER_OVERVIEW_FILE, 'r') as file:
            print(file.read())


def display_menu(current_user):
    """
    Display the appropriate menu based on user type.
    """
    print("\n" + "=" * 40)
    print("          MAIN MENU")
    print("=" * 40)
    
    if current_user == "admin":
        print("  r   - Register user")
        print("  a   - Add task")
        print("  va  - View all tasks")
        print("  vm  - View my tasks")
        print("  vc  - View completed tasks")
        print("  del - Delete task")
        print("  gr  - Generate reports")
        print("  ds  - Display statistics")
        print("  e   - Exit")
    else:
        print("  a   - Add task")
        print("  va  - View all tasks")
        print("  vm  - View my tasks")
        print("  e   - Exit")
    
    print("=" * 40)


def main():
    """
    Main program loop.
    """
    print("\n" + "=" * 50)
    print("   WELCOME TO THE TASK MANAGER SYSTEM")
    print("=" * 50)
    
    # Login
    current_user = login()
    
    # Main loop
    while True:
        display_menu(current_user)
        choice = input("\nEnter your choice: ").strip().lower()
        
        if choice == 'r':
            if current_user == "admin":
                users = read_users()
                reg_user(current_user, users)
            else:
                print("\n✗ Invalid option for your user type.")
        
        elif choice == 'a':
            add_task()
        
        elif choice == 'va':
            view_all()
        
        elif choice == 'vm':
            view_mine(current_user)
        
        elif choice == 'vc':
            if current_user == "admin":
                view_completed()
            else:
                print("\n✗ Invalid option for your user type.")
        
        elif choice == 'del':
            if current_user == "admin":
                delete_task()
            else:
                print("\n✗ Invalid option for your user type.")
        
        elif choice == 'gr':
            if current_user == "admin":
                generate_reports()
            else:
                print("\n✗ Invalid option for your user type.")
        
        elif choice == 'ds':
            if current_user == "admin":
                display_statistics()
            else:
                print("\n✗ Invalid option for your user type.")
        
        elif choice == 'e':
            print("\n" + "=" * 40)
            print("   Thank you for using Task Manager!")
            print("   Goodbye!")
            print("=" * 40)
            break
        
        else:
            print("\n✗ Invalid option. Please try again.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()