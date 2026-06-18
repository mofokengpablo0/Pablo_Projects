# Run this in Python to test if files can be read
import os

print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir())

if os.path.exists("Level 1 - Python for Software Engineering\\M03T10 – Capstone Project – Task Manager\\Code Files\\user.txt"):
    with open("Level 1 - Python for Software Engineering\\M03T10 – Capstone Project – Task Manager\\Code Files\\user.txt", 'r') as f:
        content = f.read()
        print("user.txt content:", repr(content))
else:
    print("user.txt NOT found!")

if os.path.exists("Level 1 - Python for Software Engineering\\M03T10 – Capstone Project – Task Manager\\Code Files\\tasks.txt"):
    with open("Level 1 - Python for Software Engineering\\M03T10 – Capstone Project – Task Manager\\Code Files\\tasks.txt", 'r') as f:
        content = f.read()
        print("tasks.txt content:", repr(content))
else:
    print("tasks.txt NOT found!")