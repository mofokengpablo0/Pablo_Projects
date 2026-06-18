# 📋 Task Manager — Python Capstone Project

A command-line task management application built in Python as my
capstone project at **HyperionDev**, in collaboration with the
**University of Stellenbosch Software Engineering programme**.

The application allows teams to register users, assign and track
tasks, and generate productivity reports — all from the terminal.

---

## ✨ Features

- 🔐 **User Authentication** — Secure login system using stored
  credentials in `user.txt`.
- 👥 **Role-Based Access Control** — Admins get extra privileges
  (register users, view completed tasks, delete tasks, view
  statistics).
- 📝 **Task Management (Full CRUD)** — Add, view, edit, complete,
  and delete tasks.
- 📊 **Automated Reporting** — Generates `task_overview.txt` and
  `user_overview.txt` with completion rates, overdue percentages,
  and per-user breakdowns.
- ✅ **Input Validation** — Defensive programming throughout,
  including exception handling and duplicate-username prevention.
- 🔁 **Recursive Validation** — Implemented a recursive function
  (`get_valid_task_number`) to handle invalid task selection
  gracefully.

---

## 🛠️ Tech Stack

| Category    | Tools / Concepts                              |
|-------------|-----------------------------------------------|
| Language    | Python 3                                      |
| Storage     | Text files (`.txt`) — `tasks.txt`, `user.txt` |
| Concepts    | OOP, Functions, Recursion, File I/O           |
| Practices   | PEP 8, Defensive Programming, Modular Design  |
| Versioning  | Git, GitHub                                   |

---

## 🚀 How to Run

### Prerequisites
- Python 3.x installed

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/mofokengpablo0/Pablo_Projects.git
   cd Pablo_Projects/"Task Manager"
   ```

2. **Ensure required files are in place**
   - `user.txt` (default admin: username `admin`, password `adm1n`)
   - `tasks.txt`

3. **Run the application**
   ```bash
   python task_manager.py
   ```

---

## 📂 Project Structure

```
Task Manager/
├── task_manager.py       # Main application
├── user.txt              # Stored credentials
├── tasks.txt             # Task records
├── task_overview.txt     # Generated report (after 'gr')
├── user_overview.txt     # Generated report (after 'gr')
└── README.md             # You are here
```

---

## 📖 Menu Options

### Admin User
| Option | Action                       |
|--------|------------------------------|
| `r`    | Register a new user          |
| `a`    | Add a task                   |
| `va`   | View all tasks               |
| `vm`   | View my tasks                |
| `vc`   | View completed tasks         |
| `del`  | Delete a task                |
| `ds`   | Display statistics           |
| `gr`   | Generate reports             |
| `e`    | Exit                         |

### Regular User
| Option | Action                       |
|--------|------------------------------|
| `a`    | Add a task                   |
| `va`   | View all tasks               |
| `vm`   | View my tasks                |
| `e`    | Exit                         |

---

## 🎓 What I Learned

Building this project helped me develop practical skills in:

- Structuring larger programs using **modular functions** instead
  of one long script.
- Applying **object-oriented programming** principles to model
  real-world entities (users, tasks, reports).
- Writing **defensive code** with proper exception handling and
  input validation.
- Implementing **recursion** for menu navigation — reinforcing
  the importance of clear base cases.
- Following the **PEP 8** style guide for clean, professional
  Python code.
- Managing **file I/O** for persistent storage without a
  database.

---

## 👤 Author

**Paballo Mofokeng**
📧 mofokengpablo0@gmail.com
🔗 [LinkedIn](#) *(add your LinkedIn URL here)*
💻 [GitHub](https://github.com/mofokengpablo0)

---

## 📜 License

This project was built as part of an educational programme and
is shared for portfolio purposes.
