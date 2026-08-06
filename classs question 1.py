def student_req(name, rollno):
    name= input("Enter name of the student: ")
    rollno= input("Enter the roll number of the student: ")
    print(f"Student name- {name}")
    print(f"Roll number- {rollno}")


def student_default(student_name, rollno=32):
    print(f"Student name- {student_name}")
    print(f"Roll number- {rollno}")


def student_keyword(student_name, rollno):
    print(f"Student name- {student_name}")
    print(f"Roll number- {rollno}")




def student_variable(student_name, rollno, *subjects):
        print(f"Student name- {student_name}")
        print(f"Roll number- {rollno}")
        print(f"Favourite subjects- {subjects}")


student_req("abc", "32")
student_req(name, rollno)

student_default("xyz", 42)

student_keyword(rollno=50, student_name="fgh")

student_variable("def", "45", "python", "c", "c++")
student_variable("def", "48", "math")