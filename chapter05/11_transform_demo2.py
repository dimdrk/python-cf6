def upscale_grades(grades):
    """
    Upscale grade by 1 if grade <= 9
    """
    upscaled = [grade + 1 if grade <= 9 else grade for grade in grades]
    return upscaled

def filter_passed(grades):
    """
    Filter grades (grade >= 5)
    """
    passed = [grade for grade in grades if grade >= 5]
    return passed

def categorized_grades(grades):
    """
    Categorize grades into:
    - passed: (grade >= 5 and grade < 10)
    - failed: (grade < 5)
    - honors: (grade == 10)
    """
    passed = [grade for grade in grades if grade >= 5 and grade < 10]
    failed = [grade for grade in grades if grade < 5]
    honors = [grade for grade in grades if grade == 10]

    return passed, failed, honors

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0


def main():
    grades = [7, 5, 9, 10, 3, 6, 8, 4, 10, 2]

    # Upscale grades
    upscaled_grades = upscale_grades(grades)
    print("original grades:", grades)
    print("Upscaled grades:", upscaled_grades)

    # Filter passed grades
    passed_grades = filter_passed(upscaled_grades)
    print("Passed grades:", passed_grades)

    # Categorize grades
    passed, failed, honors = categorized_grades(upscaled_grades)
    print("Passed grades:", passed)
    print("Failed grades:", failed)
    print("Honors:", honors)

if __name__ == "__main__":
    main()