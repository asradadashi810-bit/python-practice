import json


# =========================
# Course class
# =========================

class Course:

    def __init__(self, code, name, units):
        self.code = code
        self.name = name
        self.units = units

    def __str__(self):
        return f"{self.code} | {self.name} | {self.units} "

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "units": self.units
        }

# =========================
# Student class
# =========================

class Student:

    MAX_UNITS = 20

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.selected_courses = []

    def total_units(self):
        total = 0

        for course in self.selected_courses:
            total += course.units

        return total


    def add_course(self, course):

        for c in self.selected_courses:
            if c.code == course.code:
                return "This course is already selected."

        if self.total_units() + course.units > Student.MAX_UNITS:
            return "This course will exceed the maximum limit of 20 units."

        self.selected_courses.append(course)

        return "The course has been selected successfully."


    def remove_course(self, code):

        for course in self.selected_courses:

            if course.code == code:
                self.selected_courses.remove(course)
                return "removed."

        return "The course has not been selected."


    def show_courses(self):

        if len(self.selected_courses) == 0:
            return "No course has been selected."

        result = "\n Selected Course:\n"

        for course in self.selected_courses:
            result += str(course) + "\n"

        result += f"Total Units: {self.total_units()}"

        return result



# =========================
# Course selection system class
# =========================

class CourseSystem:


    def __init__(self, student):

        self.student = student
        self.courses = []


    def add_course(self, course):

        self.courses.append(course)



    def show_courses(self):

        result = "\nCourse List:\n"

        for course in self.courses:
            result += str(course) + "\n"

        return result



    def find_course(self, code):

        for course in self.courses:

            if course.code == code:
                return course

        return None



    def select_course(self, code):

        course = self.find_course(code)

        if course is None:
            return "Course code not found."

        return self.student.add_course(course)



    def remove_course(self, code):

        return self.student.remove_course(code)



    def search_course(self, text):

        result = []

        for course in self.courses:

            if text.lower() in course.name.lower():
                result.append(course)


        if len(result) == 0:
            return "No course found."


        output = "\nSearch Results:\n"

        for course in result:
            output += str(course) + "\n"

        return output



    def sort_by_units(self):

        sorted_courses = sorted(
            self.courses,
            key=lambda x: x.units
        )


        output = "\nCourses sorted by units:\n"


        for course in sorted_courses:
            output += str(course) + "\n"


        return output




# =========================
# Saving and loading data
# =========================

FILE_NAME = "data.json"



def save_data(student):

    data = {

        "name": student.name,

        "courses": [

            course.to_dict()

            for course in student.selected_courses

        ]

    }


    with open(FILE_NAME, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )





def load_data(student):

    try:

        with open(FILE_NAME, "r", encoding="utf-8") as file:

            data = json.load(file)


        student.name = data["name"]


        for c in data["courses"]:

            course = Course(
                c["code"],
                c["name"],
                c["units"]
            )

            student.selected_courses.append(course)


    except FileNotFoundError:

        pass





# =========================
# Main program
# =========================




name = input("Enter your full name: ")
student_id = input("Enter your ID: ")
student = Student(student_id, name)

load_data(student)


system = CourseSystem(student)


# Initial courses

system.add_course(Course("101", "Advanced Programming", 3))
system.add_course(Course("102", "Data Structure", 3))
system.add_course(Course("103", "Engineering Mathematics", 3))
system.add_course(Course("104", "Database", 3))
system.add_course(Course("105", "Artificial Intelligence", 3))
system.add_course(Course("106", "Computer Network", 3))
system.add_course(Course("107", "Operating System", 3))
system.add_course(Course("201", "Computer Workshop", 2))
system.add_course(Course("202", "Technical English", 2))
system.add_course(Course("301", "Programming Lab", 1))
system.add_course(Course("302", "Physical Education", 1))




while True:


    print("\n==============================")
    print("      Course Selection System")
    print("==============================")

    
    print("1- Show all courses")
    print("2- Select a course")
    print("3- Remove a course")
    print("4- Show selected courses")
    print("5- Search for a course")
    print("6- Sort courses by units")
    print("7- Show total units")
    print("8- Save information")
    print("0- Exit")


    choice = input("Enter your choice: ")



    if choice == "1":

        print(system.show_courses())



    elif choice == "2":

        code = input("Course Code: ")

        print(system.select_course(code))



    elif choice == "3":

        code = input("Enter the course code to remove: ")

        print(system.remove_course(code))



    elif choice == "4":

        print(student.show_courses())



    elif choice == "5":

        text = input("Course Name: ")

        print(system.search_course(text))



    elif choice == "6":

        print(system.sort_by_units())



    elif choice == "7":

        print(
            "Total Units:",
            student.total_units()
        )



    elif choice == "8":

        save_data(student)

        print("Saved.")



    elif choice == "0":

        save_data(student)

        print("Exit...")

        break



    else:

        print("Invalid option.")
