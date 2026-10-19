students = {
    101: {"name": "Rahul", "attendance": 85, "marks": 78},
    102: {"name": "Priya", "attendance": 90, "marks": 88},
}


def display_student(student_id):
    """Display the details for one student."""
    student = students.get(student_id)

    if student is None:
        print("Student not found.")
        return

    print(f"Student ID: {student_id}")
    print(f"Name: {student['name']}")
    print(f"Attendance: {student['attendance']}%")
    print(f"Marks: {student['marks']}")


def display_all_students():
    """Display the ID and name of every student."""
    print("All Students")
    for student_id, student in students.items():
        print(f"{student_id}: {student['name']}")


if __name__ == "__main__":
    print("College ERP System")
    selected_student_id = int(input("Enter Student ID: "))
    display_student(selected_student_id)
    display_all_students()
