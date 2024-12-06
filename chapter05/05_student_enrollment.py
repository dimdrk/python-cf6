def enroll_students(*students, min_grade=50, department="Computer Science", **kwargs):
    print(f"Min grade: {min_grade}")
    print(f"Department: {department}")
    
    print("\nEnrolled Students:")
    for student in students:
        print(f" - {student}")

    print("Additional Information")
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    print("---------------End of enrollment-------------------")
    

def main():
    enroll_students("Alice", "Bob")

    enroll_students("Helen", "Carol", "Nick", academic_year=2024, semester="Fall")

    enroll_students("Dalton", min_grade=40, department="Theater")

    enroll_students("John", "Dave", min_grade=70, department="Maths", academic_year=2025, semester="Spring")

if __name__ == "__main__":
    main()