def main():
    grades = [7, 5, 9, 10, 3]

    # Increase all grades by 1 (using list compr)
    upscaled_grades = [grade + 1 if grade <= 9 else grade for grade in grades]
    print("Upscaled grades:", upscaled_grades)

    # Increase all grades by 1 (using map func)
    upscaled_grades2 = list(map(lambda grade: grade + 1 if grade <= 9 else grade, grades))
    print("Upscaled grades 2:", upscaled_grades)

    # Filter (grades >= 5) using list compr
    passed_grades = [grade for grade in grades if grade >= 5]
    print("Passed grades:", passed_grades)

    # Filter (grades >= 5) using filter()
    passed_grades2 = list(filter(lambda grade: grade >= 5, grades))
    print("Passed grades 2:", passed_grades2)


if __name__ == "__main__":
    main()