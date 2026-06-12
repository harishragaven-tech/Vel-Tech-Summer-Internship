from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# ---------------- DATABASE CONNECTION ----------------
def get_db_connection():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn

# ---------------- CREATE TABLE ----------------
def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            rollno TEXT NOT NULL,
            department TEXT NOT NULL,
            year INTEGER NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            gender TEXT NOT NULL,
            address TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# ---------------- SAMPLE DATA ----------------
def insert_sample_data():
    conn = get_db_connection()

    existing = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]

    if existing == 0:
        conn.executemany("""
            INSERT INTO students (name, rollno, department, year, email, phone, gender, address)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            ("Rudra", "101", "CSE", 3, "rudra@veltech.edu.in", "9876543210", "Male", "Chennai"),
            ("Priyanka", "102", "IT", 2, "priya@veltech.edu.in", "9876543211", "Female", "Tambaram"),
            ("Kavin", "103", "AIML", 4, "kavin@veltech.edu.in", "9876543212", "Male", "Anna Nagar"),
            ("Harshita", "104", "ECE", 3, "harshi@veltech.edu.in", "9876543213", "Female", "Chrompet"),
            ("Ganesh", "105", "EEE", 2, "ganesh@veltech.edu.in", "9876543214", "Male", "Avadi"),
            ("Santhosh", "106", "CSE", 1, "santhosh@veltech.edu.in", "9876543215", "Male", "Velachery"),
            ("Anbu", "107", "IT", 2, "anbu@veltech.edu.in", "9876543216", "Male", "Korattur"),
            ("Robin", "108", "MECH", 4, "robin@veltech.edu.in", "9876543217", "Male", "Perungudi"),
            ("Kishore", "109", "CIVIL", 1, "kishore@veltech.edu.in", "9876543218", "Male", "Vadapalani"),
            ("Divya", "110", "AIDS", 3, "divya@veltech.edu.in", "9876543219", "Female", "Thoraipakkam")
        ])

        conn.commit()

    conn.close()

# ---------------- INIT DB (ORDER IS IMPORTANT) ----------------
init_db()
insert_sample_data()

# ---------------- ROUTES ----------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        rollno = request.form["rollno"]
        department = request.form["department"]
        year = request.form["year"]
        email = request.form["email"]
        phone = request.form["phone"]
        gender = request.form["gender"]
        address = request.form["address"]

        conn = get_db_connection()
        conn.execute("""
            INSERT INTO students (name, rollno, department, year, email, phone, gender, address)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, rollno, department, year, email, phone, gender, address))

        conn.commit()
        conn.close()

        return redirect(url_for("students"))

    return render_template("register.html")

@app.route("/students")
def students():
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("students.html", students=students)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)