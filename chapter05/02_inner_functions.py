def calculate_grade(assignments_scores, mid_score, final_score):
    def weighted_average():
        assignment_score = sum(assignments_scores) / len(assignments_scores)

        return assignment_score * 0.4 + mid_score * 0.3 + final_score * 0.3
    
    def determin_grade(average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'        
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        elif average >= 50:
            return 'E'
        else:
            return 'F'
    average = weighted_average()
    grade = determin_grade(average)

    return average, grade

def main():
    list_of_grades = [[85, 90, 88, 92], 92, 84]
    final_average, final_grade = calculate_grade([85, 90, 88, 92], 92, 84)

    print(f"Final average: {final_average}")
    print(f"Final grade: {final_grade}")

if __name__ == "__main__":
    main()