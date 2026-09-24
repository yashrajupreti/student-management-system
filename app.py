from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "student_management_secret_key"

DATABASE = "students.db"


# ---------------- DATABASE ----------------

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            course TEXT NOT NULL,
            age INTEGER,
            phone TEXT,
            attendance REAL DEFAULT 0,
            marks REAL DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


# ---------------- HOME ----------------

@app.route("/")
def home():

    conn = get_db_connection()

    total_students = conn.execute(
        "SELECT COUNT(*) FROM students"
    ).fetchone()[0]

    average_marks = conn.execute(
        "SELECT AVG(marks) FROM students"
    ).fetchone()[0]

    average_attendance = conn.execute(
        "SELECT AVG(attendance) FROM students"
    ).fetchone()[0]

    conn.close()

    if average_marks is None:
        average_marks = 0

    if average_attendance is None:
        average_attendance = 0

    return render_template(
        "index.html",
        total_students=total_students,
        average_marks=round(average_marks, 2),
        average_attendance=round(average_attendance, 2)
    )


# ---------------- ADD STUDENT ----------------

@app.route("/add_student", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        name = request.form["name"]
        roll = request.form["roll"]
        email = request.form["email"]
        course = request.form["course"]
        age = request.form["age"]
        phone = request.form["phone"]
        attendance = request.form["attendance"]
        marks = request.form["marks"]

        try:

            conn = get_db_connection()

            conn.execute("""
                INSERT INTO students
                (name, roll, email, course, age, phone, attendance, marks)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                name,
                roll,
                email,
                course,
                age,
                phone,
                attendance,
                marks
            ))

            conn.commit()
            conn.close()

            flash("Student added successfully!", "success")

            return redirect(url_for("view_students"))

        except sqlite3.IntegrityError:

            flash("Roll number already exists!", "error")

    return render_template("add_student.html")


# ---------------- VIEW STUDENTS ----------------

@app.route("/students")
def view_students():

    search = request.args.get("search", "")

    conn = get_db_connection()

    if search:

        students = conn.execute("""
            SELECT * FROM students
            WHERE name LIKE ?
            OR roll LIKE ?
            OR course LIKE ?
        """, (
            "%" + search + "%",
            "%" + search + "%",
            "%" + search + "%"
        )).fetchall()

    else:

        students = conn.execute(
            "SELECT * FROM students ORDER BY id DESC"
        ).fetchall()

    conn.close()

    return render_template(
        "students.html",
        students=students,
        search=search
    )


# ---------------- STUDENT DETAILS ----------------

@app.route("/student/<int:student_id>")
def student_details(student_id):

    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    conn.close()

    if student is None:

        flash("Student not found!", "error")

        return redirect(url_for("view_students"))

    return render_template(
        "student_details.html",
        student=student
    )


# ---------------- EDIT STUDENT ----------------

@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):

    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    if student is None:

        conn.close()

        flash("Student not found!", "error")

        return redirect(url_for("view_students"))

    if request.method == "POST":

        name = request.form["name"]
        roll = request.form["roll"]
        email = request.form["email"]
        course = request.form["course"]
        age = request.form["age"]
        phone = request.form["phone"]
        attendance = request.form["attendance"]
        marks = request.form["marks"]

        try:

            conn.execute("""
                UPDATE students
                SET name = ?,
                    roll = ?,
                    email = ?,
                    course = ?,
                    age = ?,
                    phone = ?,
                    attendance = ?,
                    marks = ?
                WHERE id = ?
            """, (
                name,
                roll,
                email,
                course,
                age,
                phone,
                attendance,
                marks,
                student_id
            ))

            conn.commit()
            conn.close()

            flash("Student updated successfully!", "success")

            return redirect(
                url_for("student_details", student_id=student_id)
            )

        except sqlite3.IntegrityError:

            flash("Roll number already exists!", "error")

    conn.close()

    return render_template(
        "edit_student.html",
        student=student
    )


# ---------------- DELETE STUDENT ----------------

@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    flash("Student deleted successfully!", "success")

    return redirect(url_for("view_students"))


# ---------------- GRADE ----------------

def calculate_grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 50:
        return "D"

    else:
        return "F"


@app.context_processor
def utility_functions():

    return dict(calculate_grade=calculate_grade)


# ---------------- START APP ----------------

if __name__ == "__main__":

    create_table()

    app.run(debug=True)