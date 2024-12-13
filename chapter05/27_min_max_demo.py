def main():
    students = {
        'Alice':85,
        'Bob':75,
        'Charlie':90,
        'David':68
    }
    
    # Find the student with the lowest grade
    student_with_lowest_grade = min(students, key=students.get)
    print("Student with lowest grade:", student_with_lowest_grade)
    
    # Find the student with the smallest name alphabetically
    student_with_smallest_name = min(students)
    print("Student with the smallest name alphabetically", student_with_smallest_name)

    # Find the student with the shortest name by length
    student_with_shortest_name = min(students, key=len)
    print("Student with the shortest name by length:", student_with_shortest_name)



if __name__ == '__main__':
    main()