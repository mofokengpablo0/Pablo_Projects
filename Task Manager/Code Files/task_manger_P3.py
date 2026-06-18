# task_manager.py
# Phase 3 - Complete Task Manager with all functionality

import os
from datetime import datetime


# ========== CONSTANTS ==========
USER_FILE = "user.txt"
TASKS_FILE = "tasks.txt"
TASK_OVERVIEW_FILE = "task_overview.txt"
USER_OVERVIEW_FILE = "user_overview.txt"
DATE_FORMAT = "%d %b %Y"


# ========== FILE OPERATIONS ==========

def read_users():
    """Load users from file. Returns {username: password}"""
    users = {}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            for line in f:
                if line.strip():
                    parts = line.strip().split(', ')
                    if len(parts) >= 2:
                        name, pwd = parts[0], parts[1]
                        users[name] = pwd
    return users



def write_user(username, password):
    """Add new user to file"""
    with open(USER_FILE, 'a') as f:
        # Ensure we start on a new line
        if os.path.exists(USER_FILE) and os.path.getsize(USER_FILE) > 0:
            f.write(f"\n{username}, {password}")
        else:
            f.write(f"{username}, {password}")



def read_tasks():
    """Load all tasks. Returns list of task dictionaries"""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            for line in f:
                if line.strip():
                    parts = line.strip().split(', ')
                    if len(parts) >= 6:
                        tasks.append({
                            "assigned_to": parts[0],
                            "title": parts[1],
                            "description": parts[2],
                            "date_assigned": parts[3],
                            "due_date": parts[4],
                            "completed": parts[5]
                        })
    return tasks



def save_tasks(tasks):
    """Save all tasks to file"""
    with open(TASKS_FILE, 'w') as f:
        for i, t in enumerate(tasks):
            f.write(f"{t['assigned_to']}, {t['title']}, {t['description']}, "
                   f"{t['date_assigned']}, {t['due_date']}, {t['completed']}")
            if i < len(tasks) - 1:
                f.write("\n")


# ========== AUTHENTICATION ==========

def login():
    """Handle user login"""
    users = read_users()
    print("\n" + "=" * 50)
    print("         TASK MANAGER LOGIN")
    print("=" * 50)
    
    while True:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if username in users and users[username] == password:
            print(f"\n[SUCCESS] Welcome, {username}!\n")
            return username
        print("\n[ERROR] Invalid credentials. Try again.\n")


# ========== MAIN MENU ==========

def show_menu(user):
    """Display appropriate menu"""
    print("\n" + "=" * 40)
    print("          MAIN MENU")
    print("=" * 40)
    print("  a  - Add task")
    print("  va - View all tasks")
    print("  vm - View my tasks")
  
    if user == "admin":
        print("  r   - Register user")
        print("  vc  - View completed tasks")
        print("  del - Delete task")
        print("  gr  - Generate reports")
        print("  ds  - Display statistics")
    
    print("  e  - Exit")
    print("=" * 40)


# ========== USER MANAGEMENT ==========

def reg_user():
    """Register new user (admin only)"""
    print("\n" + "-" * 40)
    print("        REGISTER NEW USER")
    print("-" * 40)
    
    users = read_users()
    
    while True:
        new_user = input("New username: ").strip()
        if not new_user:
            print("[ERROR] Username cannot be empty.")
            continue
        if new_user in users:
            print("[ERROR] Username exists. Try another.")
            continue
        
        password = input("Password: ").strip()
        confirm = input("Confirm password: ").strip()
        
        if not password:
            print("[ERROR] Password cannot be empty.")
            continue
        
        if password == confirm:
            write_user(new_user, password)
            print(f"\n[SUCCESS] User '{new_user}' registered!\n")
            break
        print("[ERROR] Passwords don't match.\n")


# ========== TASK MANAGEMENT ==========

def add_task():
    """Add a new task"""
    print("\n" + "-" * 40)
    print("          ADD NEW TASK")
    print("-" * 40)
    
    users = read_users()
    
    # Get assigned user
    while True:
        assigned = input("Assign to username: ").strip()
        if not assigned:
            print("[ERROR] Username cannot be empty.")
            continue
        if assigned in users:
            break
        print("[ERROR] User not found.")
    
    title = input("Task title: ").strip()
    while not title:
        title = input("Task title cannot be empty: ").strip()
    
    description = input("Description: ").strip()
    while not description:
        description = input("Description cannot be empty: ").strip()
    
    due_date = input("Due date (DD MMM YYYY): ").strip()
    while not due_date:
        due_date = input("Due date cannot be empty: ").strip()
    
    task_line = f"{assigned}, {title}, {description}, {datetime.now().strftime(DATE_FORMAT)}, {due_date}, No"
    
    # Append task to file, ensuring newline separation
    with open(TASKS_FILE, 'a') as f:
        if os.path.exists(TASKS_FILE) and os.path.getsize(TASKS_FILE) > 0:
            f.write(f"\n{task_line}")
        else:
            f.write(task_line)
    
    print("\n[SUCCESS] Task added!\n")



def view_all():
    """Display all tasks"""
    tasks = read_tasks()
    
    if not tasks:
        print("\n[INFO] No tasks found.\n")
        return
    
    print("\n" + "=" * 60)
    print("                ALL TASKS")
    print("=" * 60)
    
    for i, task in enumerate(tasks, 1):
        print(f"\n--- TASK {i} ---")
        print(f"  Title:       {task['title']}")
        print(f"  Assigned to: {task['assigned_to']}")
        print(f"  Date assigned: {task['date_assigned']}")
        print(f"  Due date:    {task['due_date']}")
        print(f"  Completed:   {task['completed']}")
        print(f"  Description: {task['description']}")
        print("-" * 60)



def view_mine(current_user):
    """View and manage user's own tasks"""
    tasks = read_tasks()
    
    # Find user's tasks
    my_tasks = []
    for i, task in enumerate(tasks):
        if task['assigned_to'] == current_user:
            my_tasks.append((i, task))
    
    if not my_tasks:
        print(f"\n[INFO] No tasks assigned to {current_user}\n")
        return
    
    # Display tasks with numbers
    print(f"\n{'=' * 60}")
    print(f"     YOUR TASKS ({current_user})")
    print(f"{'=' * 60}")
    
    for num, (idx, task) in enumerate(my_tasks, 1):
        print(f"\n--- TASK #{num} ---")
        print(f"  Title:       {task['title']}")
        print(f"  Due date:    {task['due_date']}")
        print(f"  Completed:   {task['completed']}")
        print(f"  Description: {task['description']}")
        print("-" * 50)
    
    # Get user choice
    while True:
        try:
            choice = input("\nEnter task number (-1 to exit): ").strip()
            if choice == "-1":
                return
            
            num = int(choice)
            if 1 <= num <= len(my_tasks):
                task_idx, task = my_tasks[num - 1]
                
                # Can't edit completed tasks
                if task['completed'] == "Yes":
                    print("\n[ERROR] Task already completed. Cannot edit.\n")
                    return
                
                # Edit options
                print("\n" + "-" * 30)
                print("1 - Mark as complete")
                print("2 - Edit task")
                print("-" * 30)
                
                action = input("Choice: ").strip()
                
                if action == "1":
                    tasks[task_idx]['completed'] = "Yes"
                    save_tasks(tasks)
                    print("\n[SUCCESS] Task marked complete!\n")
                    return
                
                elif action == "2":
                    edit_task(tasks, task_idx)
                    return
                else:
                    print("[ERROR] Invalid choice.")
            else:
                print(f"[ERROR] Enter 1-{len(my_tasks)} or -1")
        except ValueError:
            print("[ERROR] Enter a number")



def edit_task(tasks, task_idx):
    """Edit a task (username or due date)"""
    print("\n" + "-" * 30)
    print("1 - Change assigned user")
    print("2 - Change due date")
    print("3 - Change both")
    print("-" * 30)
    
    choice = input("Choice: ").strip()
    users = read_users()
    
    if choice in ["1", "3"]:
        new_user = input("New assigned user: ").strip()
        if new_user in users:
            tasks[task_idx]['assigned_to'] = new_user
            print("[SUCCESS] User updated")
        else:
            print("[ERROR] User not found")
    
    if choice in ["2", "3"]:
        new_date = input("New due date (DD MMM YYYY): ").strip()
        tasks[task_idx]['due_date'] = new_date
        print("[SUCCESS] Due date updated")
    
    save_tasks(tasks)
    print("\n[SUCCESS] Task updated!\n")



def view_completed():
    """Show all completed tasks (admin only)"""
    tasks = read_tasks()
    completed = [t for t in tasks if t['completed'] == "Yes"]
    
    if not completed:
        print("\n[INFO] No completed tasks.\n")
        return
    
    print("\n" + "=" * 60)
    print("          COMPLETED TASKS")
    print("=" * 60)
    
    for i, task in enumerate(completed, 1):
        print(f"\n--- COMPLETED TASK {i} ---")
        print(f"  Title:       {task['title']}")
        print(f"  Assigned to: {task['assigned_to']}")
        print(f"  Due date:    {task['due_date']}")
        print(f"  Completed:   {task['completed']}")
        print("-" * 50)



def delete_task():
    """Delete a task (admin only)"""
    tasks = read_tasks()
    
    if not tasks:
        print("\n[INFO] No tasks to delete.\n")
        return
    
    # Show all tasks with numbers
    print("\n" + "=" * 60)
    print("           DELETE TASK")
    print("=" * 60)
    
    for i, task in enumerate(tasks, 1):
        print(f"\n{i}. {task['title']} (assigned to: {task['assigned_to']})")
        print(f"   Due: {task['due_date']} | Completed: {task['completed']}")
    
    try:
        choice = input("\nTask number to delete (-1 to cancel): ").strip()
        if choice == "-1":
            return
        
        num = int(choice)
        if 1 <= num <= len(tasks):
            confirm = input(f"Delete '{tasks[num-1]['title']}'? (y/n): ").lower()
            if confirm == 'y':
                tasks.pop(num-1)
                save_tasks(tasks)
                print("\n[SUCCESS] Task deleted!\n")
            else:
                print("Cancelled.")
        else:
            print("[ERROR] Invalid number")
    except ValueError:
        print("[ERROR] Enter a number")


# ========== REPORTS & STATISTICS ==========

def generate_reports():
    """Create task_overview.txt and user_overview.txt"""
    tasks = read_tasks()
    users = read_users()
    total_tasks = len(tasks)
    today = datetime.now()
    
    # Task calculations
    completed = sum(1 for t in tasks if t['completed'] == "Yes")
    uncompleted = total_tasks - completed
    
    overdue = 0
    for t in tasks:
        if t['completed'] == "No":
            try:
                if datetime.strptime(t['due_date'], DATE_FORMAT) < today:
                    overdue += 1
            except:
                pass
    
    # Calculate percentages
    incomplete_percent = (uncompleted / total_tasks * 100) if total_tasks > 0 else 0
    overdue_percent = (overdue / total_tasks * 100) if total_tasks > 0 else 0
    
    # TASK OVERVIEW
    with open(TASK_OVERVIEW_FILE, 'w') as f:
        f.write("=" * 50 + "\n")
        f.write("        TASK OVERVIEW REPORT\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Total number of tasks:           {total_tasks}\n")
        f.write(f"Total number of completed tasks: {completed}\n")
        f.write(f"Total number of uncompleted tasks: {uncompleted}\n")
        f.write(f"Total number of overdue tasks:   {overdue}\n")
        f.write(f"Percentage of incomplete tasks:  {incomplete_percent:.1f}%\n")
        f.write(f"Percentage of overdue tasks:     {overdue_percent:.1f}%\n")
    
    # USER OVERVIEW
    with open(USER_OVERVIEW_FILE, 'w') as f:
        f.write("=" * 50 + "\n")
        f.write("        USER OVERVIEW REPORT\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Total number of users registered: {len(users)}\n")
        f.write(f"Total number of tasks:            {total_tasks}\n\n")
        f.write("-" * 40 + "\n")
        
        for user in users:
            user_tasks = [t for t in tasks if t['assigned_to'] == user]
            count = len(user_tasks)
            
            # Calculate user statistics
            percent_of_total = (count / total_tasks * 100) if total_tasks > 0 else 0
            
            user_completed = sum(1 for t in user_tasks if t['completed'] == "Yes")
            percent_completed = (user_completed / count * 100) if count > 0 else 0
            percent_incomplete = 100 - percent_completed if count > 0 else 0
            
            # Count overdue for user
            user_overdue = 0
            for t in user_tasks:
                if t['completed'] == "No":
                    try:
                        if datetime.strptime(t['due_date'], DATE_FORMAT) < today:
                            user_overdue += 1
                    except:
                        pass
            
            percent_overdue = (user_overdue / count * 100) if count > 0 else 0
            
            f.write(f"\n[USER: {user}]\n")
            f.write(f"  - Total tasks assigned:        {count}\n")
            f.write(f"  - Percentage of total tasks:   {percent_of_total:.1f}%\n")
            f.write(f"  - Percentage completed:        {percent_completed:.1f}%\n")
            f.write(f"  - Percentage incomplete:       {percent_incomplete:.1f}%\n")
            f.write(f"  - Percentage incomplete & overdue: {percent_overdue:.1f}%\n")
    
    print(f"\n[SUCCESS] Reports generated successfully!")
    print(f"  - {TASK_OVERVIEW_FILE}")
    print(f"  - {USER_OVERVIEW_FILE}\n")



def display_statistics():
    """Show statistics (generate reports if needed)"""
    if not os.path.exists(TASK_OVERVIEW_FILE) or not os.path.exists(USER_OVERVIEW_FILE):
        print("\n[INFO] Reports not found. Generating them now...")
        generate_reports()
    
    print("\n" + "=" * 60)
    print("           SYSTEM STATISTICS")
    print("=" * 60)
    
    # Display task overview
    if os.path.exists(TASK_OVERVIEW_FILE):
        with open(TASK_OVERVIEW_FILE, 'r') as f:
            print(f.read())
    
    # Display user overview
    if os.path.exists(USER_OVERVIEW_FILE):
        with open(USER_OVERVIEW_FILE, 'r') as f:
            print(f.read())


# ========== MAIN PROGRAM ==========

def main():
    """Main program loop"""
    print("\n" + "=" * 50)
    print("   TASK MANAGER - PHASE 3")
    print("=" * 50)
    
    current_user = login()
    
    while True:
        show_menu(current_user)
        choice = input("\nYour choice: ").strip().lower()
        
        # Common options (all users)
        if choice == 'a':
            add_task()
        elif choice == 'va':
            view_all()
        elif choice == 'vm':
            view_mine(current_user)
        elif choice == 'e':
            print("\n[INFO] Goodbye!\n")
            break
        
        # Admin-only options
        elif current_user == "admin":
            if choice == 'r':
                reg_user()
            elif choice == 'vc':
                view_completed()
            elif choice == 'del':
                delete_task()
            elif choice == 'gr':
                generate_reports()
            elif choice == 'ds':
                display_statistics()
            else:
                print("\n[ERROR] Invalid option.\n")
        else:
            print("\n[ERROR] Invalid option.\n")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()