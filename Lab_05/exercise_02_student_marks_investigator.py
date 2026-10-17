# Lab 05 - Exercise 2: Student Marks Investigator
students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]],
]


def calculate_average(marks):
    if not marks or len(marks) != 3:
        return None
    if any(not isinstance(mark, (int, float)) or not 0 <= mark <= 100 for mark in marks):
        return None
    return sum(marks) / len(marks)


def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    return "Needs Improvement"


def display_report(students):
    if not students:
        print("No student records found.")
        return
    for student_id, name, marks in students:
        average = calculate_average(marks)
        if average is None:
            print(f"ID: {student_id}, Name: {name}, Invalid or missing marks")
        else:
            category = classify_performance(average)
            print(f"ID: {student_id}, Name: {name}, Average: {average:.2f}, Performance: {category}")


if __name__ == "__main__":
    print("Student performance report:")
    display_report(students)
    print("\nTest cases: equal marks, tied averages, invalid marks, missing marks")
    test_students = [
        [206, "Sami", [80, 80, 80]],
        [207, "Rafi", [90, 70, 80]],
        [208, "Karim", [90, 110, 75]],
        [209, "Mina", []],
    ]
    display_report(test_students)
