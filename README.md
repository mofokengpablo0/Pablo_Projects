# Paballo Mofokeng | Pablo_Projects

### *From the print floor to the pull request.*
*Precision learned on a production line. Applied to every line of code.*

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![REST API](https://img.shields.io/badge/Django_REST_Framework-A30000?style=flat)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=flat&logo=mariadb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)

---

## About me

I'm a junior software engineer from Vanderbijlpark, Gauteng. I recently completed the **Stellenbosch University Software Engineering Bootcamp (HyperionDev)** with a **99% average, ranking 9th of 79 students**.

Before writing code full-time, I spent 2025 as a multi-role intern at Java Prints, where I quality-controlled labels for retailers like Pick n Pay, Checkers and Woolworths and managed stock on a busy production floor. That's where I learned accuracy, accountability and working to deadlines. I now bring the same habits to software: testing, validating input and documenting my work.

I'm looking for my first junior software engineering role, in Gauteng or remote.

**Contact:** [LinkedIn](https://www.linkedin.com/in/paballo-mofokeng) | mofokengpablo0@gmail.com | [HyperionDev Portfolio](https://www.hyperiondev.com/portfolio/PM26020019904/)

---

## Featured project

### News_App | Django News Platform
*A role-based news platform with a REST API, automated tests and Docker.*

Journalists write articles, editors approve them, and readers subscribe to the publishers and journalists they follow.

**Key features**
- **Three user roles:** Reader, Editor and Journalist, using a custom user model and Django groups and permissions.
- **Article workflow:** Journalists create articles and editors review and approve them before readers see them.
- **Subscriptions:** Readers can follow publishers and individual journalists.
- **RESTful API:** Built with Django REST Framework, with token authentication, role-based authorisation and serializers so third-party clients can retrieve and manage articles.
- **Automation:** Subscribers are emailed when an editor approves an article, and the approval is logged to an internal API endpoint.
- **Automated tests:** Unit tests cover role-based access, subscriptions and approval logic, and use mocking for email and API calls.
- **Production-minded setup:** MariaDB database, Docker container, Sphinx documentation and Git branch-based development.

**Tech stack:** Python, Django, Django REST Framework, MariaDB, Docker, Sphinx, Git

**Run it locally**
```bash
git clone https://github.com/mofokengpablo0/Pablo_Projects.git
cd Pablo_Projects/News_App
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Run with Docker**
```bash
docker build -t news-app .
docker run -p 8000:8000 news-app
```

---

## More projects

### Team Task Manager | Python
A command-line task manager with user authentication and role-based access (admin and user). It supports the full task lifecycle (create, view, edit, complete, delete), blocks duplicate usernames, and generates reports showing completion rates and overdue-task percentages.
**Skills shown:** exception handling, input validation, recursion, modular code (PEP 8).

### Retail Inventory Management System | Python
An inventory app for tracking stock levels and replacing manual record-keeping, with full CRUD operations (add, update, view, remove products). It's structured into reusable classes using object-oriented principles, and it was inspired by my stock-management work at Java Prints.
**Skills shown:** object-oriented programming, CRUD logic, clean code structure.

---

## Skills

| Area | Tools |
|---|---|
| **Languages** | Python, Java, SQL, HTML, CSS |
| **Frameworks** | Django, Django REST Framework, Bootstrap |
| **Databases** | MariaDB, SQLite |
| **DevOps & tools** | Docker, Git, GitHub, shell scripting, Visual Studio Code |
| **Practices** | Unit testing, object-oriented design, documentation (Sphinx), debugging |

---

## Education

- **Software Engineering Bootcamp:** Stellenbosch University (Online) | HyperionDev, 2026. 99% average, ranked 9th of 79.
- **National Senior Certificate:** Hoërskool Suiderlig, 2025.

---

## Let's talk

If you're hiring junior developers and want someone who learns quickly, tests their code and takes pride in accuracy, I'd love to hear from you.

**[Connect on LinkedIn](https://www.linkedin.com/in/paballo-mofokeng) | [Email me](mailto:mofokengpablo0@gmail.com)**
