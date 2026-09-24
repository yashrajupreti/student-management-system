import sqlite3
import random

DATABASE = "students.db"


# -----------------------------
# SAMPLE DATA
# -----------------------------

first_names = [
    "Yash", "Rahul", "Aman", "Priya", "Neha",
    "Rohit", "Anjali", "Arjun", "Karan", "Simran",
    "Vikas", "Pooja", "Aditya", "Sneha", "Riya",
    "Mohit", "Nikhil", "Kavya", "Ayush", "Ishita",
    "Varun", "Shreya", "Akash", "Muskan", "Sahil",
    "Tanvi", "Harsh", "Megha", "Abhishek", "Nisha"
]

last_names = [
    "Sharma", "Verma", "Gupta", "Singh", "Kumar",
    "Mehta", "Joshi", "Patel", "Agarwal", "Jain",
    "Choudhary", "Yadav", "Mishra", "Bansal", "Saini"
]

courses = [
    "BCA",
    "B.Tech",
    "MCA",
    "BBA",
    "MBA",
    "B.Sc",
    "M.Sc",
    "B.Com",
    "M.Com"
]


# -----------------------------
# CONNECT DATABASE
# -----------------------------

conn = sqlite3.connect(DATABASE)

cursor = conn.cursor()


# -----------------------------
# MAKE SURE TABLE EXISTS
# -----------------------------

cursor.execute("""
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


# -----------------------------
# INSERT 200 STUDENTS
# -----------------------------

students_added = 0

for i in range(1, 201):

    first_name = random.choice(first_names)

    last_name = random.choice(last_names)

    name = first_name + " " + last_name

    roll = "STU" + str(i).zfill(3)

    email = (
        first_name.lower()
        + str(i)
        + "@studenthub.com"
    )

    course = random.choice(courses)

    age = random.randint(18, 24)

    phone = "9" + str(
        random.randint(100000000, 999999999)
    )

    attendance = round(
        random.uniform(55, 98),
        2
    )

    marks = round(
        random.uniform(35, 98),
        2
    )


    try:

        cursor.execute("""
            INSERT INTO students
            (
                name,
                roll,
                email,
                course,
                age,
                phone,
                attendance,
                marks
            )

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

        students_added += 1


    except sqlite3.IntegrityError:

        pass


# -----------------------------
# SAVE
# -----------------------------

conn.commit()


# -----------------------------
# CHECK TOTAL
# -----------------------------

total = cursor.execute(
    "SELECT COUNT(*) FROM students"
).fetchone()[0]


conn.close()


print("--------------------------------")
print("Student data generation complete!")
print("--------------------------------")
print("New students added:", students_added)
print("Total students in database:", total)
print("--------------------------------")