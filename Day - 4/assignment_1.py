students = [
    {"name": "Tarun", "marks": [80, 72, 91]},
    {"name": "Ashmita", "marks": [65, 88, 79]},
    {"name": "Alinda", "marks": [35, 42, 38]},
    {"name": "Pritam", "marks": [79, 41, 26]},
    {"name": "Anirban", "marks": [81, 91, 31]},
]

# Calculate average marks
def calculate_average(marks):
    average = sum(marks) / len(marks)
    return average

# Determine PASS/FAIL
def is_pass(marks):
    average = calculate_average(marks)
    if average >= 40:
        return "PASS"
    return "FAIL"

# Find the topper
def find_topper(students):
    topper = None
    highest_average = 0
    for student in students:
        average = calculate_average(student["marks"])
        if average > highest_average:
            highest_average = average
            topper = student
    return topper["name"]  

# Find the lowest-performing student
def find_lowest(students):
    lowest_student = None
    lowest_average = float("inf") 
    for student in students:
        average = calculate_average(student["marks"]) 
        if average < lowest_average:
            lowest_average = average
            lowest_student = student
    return lowest_student["name"]   

# Calculate class average
def calculate_class_average(students):
    total = 0
    for student in students:
        average = calculate_average(student["marks"])
        total += average
    class_average = total / len(students)
    return class_average

# Calling the functions
print(calculate_average(students[4]["marks"]))
print(is_pass(students[0]["marks"]))
print(find_topper(students))
print(find_lowest(students))
print(calculate_class_average(students))




# class version
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # average marks
    def calculate_average(self):
        average = sum(self.marks) / len(self.marks)
        return average

    # Determine PASS/FAIL
    def is_pass(self):
        average = self.calculate_average()

        if average >= 40:
            return "PASS"

        return "FAIL"


class StudentAnalyzer:

    # the topper
    def find_topper(self, students):
        topper = None
        highest_average = 0

        for student in students:
            average = student.calculate_average()

            if average > highest_average:
                highest_average = average
                topper = student

        return topper.name

    # lowest-performing student
    def find_lowest(self, students):
        lowest_student = None
        lowest_average = float("inf")

        for student in students:
            average = student.calculate_average()

            if average < lowest_average:
                lowest_average = average
                lowest_student = student

        return lowest_student.name

    # Calculate class average
    def calculate_class_average(self, students):
        total = 0

        for student in students:
            average = student.calculate_average()
            total += average

        class_average = total / len(students)

        return class_average


# Creating student objects
students = [
    Student("Tarun", [80, 72, 91]),
    Student("Ashmita", [65, 88, 79]),
    Student("Alinda", [35, 42, 38]),
    Student("Pritam", [79, 41, 26]),
    Student("Anirban", [81, 91, 31])
]

# Creating analyzer object
analyzer = StudentAnalyzer()

# Calling the methods
print(students[4].calculate_average())
print(students[0].is_pass())
print(analyzer.find_topper(students))
print(analyzer.find_lowest(students))
print(analyzer.calculate_class_average(students))