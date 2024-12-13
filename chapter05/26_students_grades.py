students = {
    'Alice':[85, 92, 78],       # 85.00
    'Bob':[79, 95, 88],         # 87.33
    'Charlie':[68, 72, 80],     # 73.33
    'Diana':[95, 98, 100],      # 97.67
    'Eve':[50, 68, 58]          # 58.67
}

def main():
    # threshold
    threshold = int(input("Please insert a threshold (int):"))      # insert 75 for example presentation

    average_grades = { student: round(sum(grades) / len(grades), 2) for student, grades in students.items()
                      if round(sum(grades) / len(grades), 2) > threshold}
    print(average_grades)

    for student, grade in average_grades.items():
        print(f"{student} : {grade}")

if __name__ == '__main__':
    main()