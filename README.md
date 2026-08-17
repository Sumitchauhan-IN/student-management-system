# Student Management System

A full-stack web application built with **Django** and **MySQL** for managing student records, courses, marks, and attendance. Includes user authentication, complete CRUD functionality, and search capabilities.

## Features

- **User Authentication** – Secure login/logout system; all pages protected for logged-in users only
- **Student Management** – Add, edit, delete, and view student records
- **Course Management** – Students linked to courses via foreign key relationships
- **Marks Tracking** – Record subject-wise marks with automatic percentage calculation
- **Attendance Tracking** – Mark and view student attendance (Present/Absent)
- **Search Functionality** – Search students by name or roll number
- **Responsive UI** – Built with Bootstrap 5

## Tech Stack

- **Backend:** Python, Django
- **Database:** MySQL
- **Frontend:** HTML, CSS, Bootstrap 5
- **Version Control:** Git & GitHub

## Database Schema

- **Student** – name, roll number, email, phone, course (FK), date joined
- **Course** – course name, duration
- **Marks** – student (FK), subject, marks obtained, total marks
- **Attendance** – student (FK), date, status

## Installation & Setup

1. **Clone the repository**
```bash
   git clone https://github.com/Sumitchauhan-IN/student-management-system.git
   cd student-management-system
```

2. **Create and activate a virtual environment**
```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
```

3. **Install dependencies**
```bash
   pip install django mysqlclient
```

4. **Set up MySQL database**
```sql
   CREATE DATABASE student_db;
```

5. **Configure database settings**

   Update `core/settings.py` with your MySQL credentials:
```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'student_db',
           'USER': 'root',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
```

6. **Run migrations**
```bash
   python manage.py makemigrations
   python manage.py migrate
```

7. **Create a superuser (admin account)**
```bash
   python manage.py createsuperuser
```

8. **Run the development server**
```bash
   python manage.py runserver
```

9. Visit `http://127.0.0.1:8000/` in your browser.

## Screenshots

*(Add screenshots of your Student List, Add Student form, Marks page, and Attendance page here)*

## Future Improvements

- Role-based access (Admin vs Teacher views)
- PDF report generation for student results
- Pagination for large datasets
- REST API for mobile integration

## Author

**Bhavanand Chauhan**  
GitHub: [@Sumitchauhan-IN](https://github.com/Sumitchauhan-IN)