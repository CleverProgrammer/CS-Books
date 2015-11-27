"""
Author: Rafeh Qazi
Create a student class that models a student.
Date: 11/26/2015
"""
import os
from collections import namedtuple


def all_student_results(students_file):
    """
    Read file and return students' first-name, last-name, hours,
    and the quality points.
    :param students_file: string
    :return all_students: dict
    :return default_student: str
    """
    if os.stat(students_file).st_size == 0:
        raise UnboundLocalError('Empty File')

    Student_info = namedtuple('Student_info', 'last_name first_name hours q_points')
    all_students = dict()
    with open(students_file, mode='r') as f:
        for line in f:
            line = Student_info(*line.split())
            all_students[line.first_name] = line[0][:-1], line.hours, line.q_points
            default_student = line.first_name
    return all_students, default_student


def best_student(default_student, all_students):
    """
    Take all_students as input and return the student key with the
    best GPA.
    :param all_students: dict
    :param default_student: str
    :return all_students[top_student]: dict
    :return top_student_gpa: float
    """
    top_student = default_student
    # All_students = namedtuple('All_Students', 'last_name hours quality_points')
    for student in all_students:
        student_result = float(all_students[student][2]) / float(all_students[student][1])
        top_student_result = float(all_students[top_student][2]) / float(all_students[top_student][1])
        if student_result > top_student_result:
            top_student = student
    return all_students[top_student], float(all_students[top_student][2]) / float(all_students[top_student][1])


def print_results(top_student, top_student_gpa):
    """
    Take the student with the highest GPA and print their report.
    Print the report of the best student.
    :param top_student: object
    """
    print('The best student is {0}, who has spent {1} hours and has a {2} gpa.'.format(
        top_student[0], top_student[1], top_student_gpa))


def main():
    all_students, default_student = all_student_results('students.txt')
    top_student, top_student_gpa = best_student(default_student, all_students)
    print_results(top_student, top_student_gpa)

if __name__ == '__main__':
    main()
