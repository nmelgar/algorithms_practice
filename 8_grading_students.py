"""
- Every student receives a  grade in the inclusive range 
from 0 to 100
- Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each 
student's grade according to these rules:
- If the difference between the grade and the next multiple 
of 5 is less than 3, round grade up to the next multiple 
of 5.
- If the value of grade is less than 38, no rounding occurs 
as the result will still be a failing grade.

Examples:
84 round  to 85  (85 - 84 is less than 3)
29 do not round (result is less than 40)
57 do not round (60 - 57 is 3 or higher) 
"""


def main():
    grades = [73, 67, 38, 33]
    gradingStudents(grades)


def gradingStudents(grades):
    MULTIPLE = 5
    for grade in grades:
        index = grades.index(grade)
        missing = grade % 5
        if missing >= 3:
            next_multiple = MULTIPLE - missing
            new_grade = grade + next_multiple
            if new_grade >= 40:
                grades.pop(index)
                grades.insert(index, new_grade)
            else:
                pass
        elif missing < 3:
            pass
    return grades

    # for grade in grades:
    #     missing = grade % 5
    #     if missing >= 3:
    #         next_multiple = MULTIPLE - missing
    #         new_grade = grade + next_multiple
    #         if new_grade >= 40:
    #             print(new_grade)
    #         else:
    #             print(grade)
    #     elif missing < 3:
    #         print(grade)


if __name__ == "__main__":
    main()
