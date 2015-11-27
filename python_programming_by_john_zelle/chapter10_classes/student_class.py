"""
Author: Rafeh Qazi
Create a student class that models a student.
Date: 11/26/2015
"""
from collections import namedtuple


class Student:
    def __init__(self, name, hours, quality_points):
        self.name = name
        self.hours = float(hours)
        self.quality_points = float(quality_points)

    def result(self):
        return self.quality_points / self.hours


def all_student_results(filename):
    """
    Read file and return students' first-name, last-name, hours,
    and the quality points.
    :param filename: string
    :return: list
    """
    Student_info = namedtuple('Student_info',
                              'last_name first_name hours q_points')
    all_students = []
    with open(filename, mode='r') as f:
        for line in f:
            line = Student_info(*line.split())
            student = Student(line.last_name, line.hours, line.q_points)
            all_students.append(student)
    return all_students


def best_student(all_students):
    """
    Take all_students as input and return the student with the
    best GPA.
    :param all_students: list
    """
    top_student = all_students[0]
    for student in all_students:
        if student.result() > top_student.result():
            top_student = student
    return top_student


def print_results(top_student):
    """
    Take the student with the highest GPA and print their report.
    Print the report of the best student.
    :param top_student: object
    """
    print('The best student is {0} who has spent {1} hours and has a {2} gpa.'.format(
        top_student.name, top_student.hours, top_student.result()))


def main():
    all_students = all_student_results('students.txt')
    top_student = best_student(all_students)
    print_results(top_student)

if __name__ == '__main__':
    main()
