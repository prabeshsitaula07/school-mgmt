class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"{course} added to {self.name}'s course list.")

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"{course} dropped from {self.name}'s course list.")
        else:
            print(f"{self.name} is not enrolled in {course}.")

    def display_courses(self):
        if self.courses:
            print(f"{self.name}'s Enrolled Courses:")
            for course in self.courses:
                print("- ", course)
        else:
            print(f"{self.name} is not enrolled in any courses.")


class Course:
    def __init__(self, name, instructor):
        self.name = name
        self.instructor = instructor
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)
        print(f"{student.name} enrolled in {self.name}.")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"{student.name} removed from {self.name}.")
        else:
            print(f"{student.name} is not enrolled in {self.name}.")

    def display_students(self):
        if self.students:
            print(f"Students Enrolled in {self.name}:")
            for student in self.students:
                print("- ", student.name)
        else:
            print(f"No students enrolled in {self.name}.")


def main():
    students = []
    courses = []

    while True:
        print("\n---- School Management System ----")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. Remove Student from Course")
        print("5. Display Student's Courses")
        print("6. Display Course's Students")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        print()

        if choice == "1":
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = int(input("Enter student's grade: "))
            student = Student(name, age, grade)
            students.append(student)
            print(f"{name} added as a student.")

        elif choice == "2":
            name = input("Enter course name: ")
            instructor = input("Enter instructor's name: ")
            course = Course(name, instructor)
            courses.append(course)
            print(f"{name} course added.")

        elif choice == "3":
            student_name = input("Enter student's name: ")
            course_name = input("Enter course name: ")
            student = next((s for s in students if s.name == student_name), None)
            course = next((c for c in courses if c.name == course_name), None)
            if student and course:
                course.enroll_student(student)
                student.add_course(course.name)
            else:
                print("Student or course not found.")

        elif choice == "4":
            student_name = input("Enter student's name: ")
            course_name = input("Enter course name: ")
            student = next((s for s in students if s.name == student_name), None)
            course = next((c for c in courses if c.name == course_name), None)
            if student and course:
                course.remove_student(student)
                student.drop_course(course.name)
            else:
                print("Student or course not found.")

        elif choice == "5":
            student_name = input("Enter student's name: ")
            student = next((s for s in students if s.name == student_name), None)
            if student:
                student.display_courses()
            else:
                print("Student not found.")

        elif choice == "6":
            course_name = input("Enter course name: ")
            course = next((c for c in courses if c.name == course_name), None)
            if course:
                course.display_students()
            else:
                print("Course not found.")

        elif choice == "7":
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
