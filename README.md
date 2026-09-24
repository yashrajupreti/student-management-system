# 🎓 Student Management System

A web-based **Student Management System** developed using **Python, Flask, HTML, CSS, and SQLite**.

This application provides a simple web interface for managing student records. It allows student information to be added, viewed, updated, searched, and deleted while also keeping track of marks and attendance.

The project uses **Flask** to handle the backend and routing, **HTML/Jinja templates** for the frontend, **CSS** for the user interface, and **SQLite** for storing student data.

---

## 📌 Project Overview

Managing student information manually can become difficult when the number of records increases. This project provides a centralized system where student information can be stored and managed through a web application.

The system maintains important student information such as:

* Student ID
* Student Name
* Roll Number
* Email
* Course
* Age
* Phone Number
* Attendance
* Marks

The application also provides a dashboard that displays useful overall statistics from the stored student records.

---

## ✨ Features

### 🏠 Dashboard

The dashboard provides an overview of the student database.

It displays:

* **Total Students**
* **Average Marks**
* **Average Attendance**

The average marks and attendance are calculated directly from the student records stored in the SQLite database.

---

### ➕ Add Student

The application provides a form for adding new student records.

The form accepts information such as:

* Name
* Roll Number
* Email
* Course
* Age
* Phone Number
* Attendance
* Marks

The information submitted through the form is stored in the SQLite database.

---

### 👥 View Students

The system provides a dedicated student management page where stored student records can be viewed.

This allows users to easily see the available student information and access management options for individual records.

---

### 🔍 Search and Filter Students

The application provides student search/filter functionality.

Users can search the available records to find specific students instead of manually going through every record.

---

### 📄 Student Details

Individual student information can be viewed through a dedicated student details page.

This provides a more detailed view of a selected student's information.

---

### ✏️ Update Student Information

Existing student records can be edited when information needs to be changed.

This allows details such as:

* Name
* Email
* Course
* Age
* Phone
* Attendance
* Marks

to be updated.

---

### 🗑️ Delete Students

The system allows student records to be deleted from the database when they are no longer required.

---

### 📊 Marks and Attendance

The system stores both **marks** and **attendance** for every student.

These values are also used by the dashboard to calculate:

* Average marks
* Average attendance

---

### 🗄️ SQLite Database

The project uses **SQLite** as its database.

The `students` table contains fields for:

| Field        | Description          |
| ------------ | -------------------- |
| `id`         | Unique student ID    |
| `name`       | Student name         |
| `roll`       | Unique roll number   |
| `email`      | Student email        |
| `course`     | Student course       |
| `age`        | Student age          |
| `phone`      | Student phone number |
| `attendance` | Student attendance   |
| `marks`      | Student marks        |

The roll number is configured as a unique field to prevent duplicate roll numbers.

---

## 🛠️ Technologies Used

| Technology | Purpose                    |
| ---------- | -------------------------- |
| **Python** | Backend programming        |
| **Flask**  | Web application framework  |
| **HTML**   | Web page structure         |
| **CSS**    | User interface and styling |
| **Jinja2** | Dynamic HTML templates     |
| **SQLite** | Database management        |

---

## 📂 Project Structure

```text
student-management-system/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── add_student.html
│   ├── base.html
│   ├── edit_student.html
│   ├── index.html
│   ├── student_details.html
│   └── students.html
│
├── app.py
├── seed_data.py
├── students.db
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔧 How the Application Works

The application follows a simple client-server-database flow:

```text
User
  ↓
Web Browser
  ↓
Flask Application
  ↓
Python Backend
  ↓
SQLite Database
  ↓
Student Records
```

### Backend

`app.py` contains the Flask application and handles:

* Application routes
* Database connection
* Student creation
* Student retrieval
* Student updates
* Student deletion
* Search/filter operations
* Dashboard statistics

### Frontend

The `templates` folder contains the HTML pages used by the application.

Jinja2 templates are used to display dynamic information received from Flask.

### Styling

The `static/style.css` file contains the styling for the application's interface, including layout, navigation, buttons, and other visual elements.

---

## 🌱 Sample Data Generation

The project also contains:

```text
seed_data.py
```

This script is used to generate sample student records for testing and demonstration purposes.

It creates sample student information and stores it in the SQLite database.

This makes it easier to test the application with a larger number of student records without entering every record manually.

---

## 🚀 Installation and Setup

### 1. Download or Clone the Repository

Download this repository to your computer and open the project folder.

### 2. Install Required Package

Open a terminal inside the project folder and run:

```bash
pip install -r requirements.txt
```

The project uses Flask as its external Python dependency.

### 3. Generate Sample Data

If sample data is required, run:

```bash
python seed_data.py
```

This will populate the SQLite database with sample student records.

### 4. Run the Application

Start the Flask application using:

```bash
python app.py
```

### 5. Open the Website

After starting Flask, open the local address shown in the terminal in your web browser.

Usually, the application runs at:

```text
http://127.0.0.1:5000/
```

---

## 🧪 Database Initialization

The Flask application checks for the required `students` table and creates it if it does not already exist.

The database is stored locally in:

```text
students.db
```

This allows student information to remain available between application runs.

---

## 📱 User Interface

The application includes separate pages for different operations:

```text
Dashboard
   │
   ├── View Students
   │      ├── Search / Filter
   │      ├── Student Details
   │      ├── Edit Student
   │      └── Delete Student
   │
   └── Add Student
```

The application uses a common base template and separate templates for individual student-management operations.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Build a functional web application using Flask.
* Learn how a Python backend communicates with a database.
* Implement CRUD operations.
* Work with SQLite databases.
* Handle HTML forms using Flask.
* Use Jinja2 templates for dynamic web pages.
* Create a structured frontend using HTML and CSS.
* Practice connecting frontend, backend, and database components together.

---

## 📚 What I Learned

Through this project, I practiced:

* Python
* Flask
* Routing
* HTML forms
* Jinja2 templating
* SQLite
* SQL queries
* CRUD operations
* Database connections
* Form handling
* Dynamic web pages
* CSS styling
* Organizing a Flask project

---

## 👨‍💻 Author

**Yash Raj Upreti**

GitHub: [yashrajupreti](https://github.com/yashrajupreti)

---

## ⭐ Project Repository

If you find this project useful or interesting, feel free to explore the repository and give it a star.

**Repository:**
https://github.com/yashrajupreti/student-management-system
