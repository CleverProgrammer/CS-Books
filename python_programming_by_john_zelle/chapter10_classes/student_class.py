"""
Author: Rafeh Qazi
Create a student class that models a student.
Date: 11/26/2015
Function_Based_Gist: https://gist.github.com/Rafeh01/4a6d6b79eee4caf6b799
Update: 11/27/2015
Final_Gist: https://gist.github.com/Rafeh01/57fc4c710bf9322d75db
Key Features:
1. Class
2. Class Object Counter
3. @classmethod Decorators
4. Selection Sort
5. namedtuples
6. Tuple Unpacking
7. Context Manager
8. Methods taking class
9. pep8 Do Not Exceed Line Beauties
10. Solid Documentation
11. String Formatting
12. Used classmethods to improve readibility
13. Emphasis on readability
"""
from collections import namedtuple


class Student:
    """
    A student class that models a student.

    >>> qazi = Student('rafeh', 40, 100)
    >>> qazi.name
    'rafeh'
    >>> qazi.hours
    40.0
    >>> qazi.quality_points
    100.0
    >>> qazi.gpa
    2.5
    >>> nick = Student('drane', 20, 100)
    >>> nick.gpa
    5.0
    >>> Student.top_student.name
    'drane'
    """

    student_counter = 0
    all_students = []
    top_student = None

    def __init__(self, name, hours, quality_points):
        self.name = name
        self.hours = float(hours)
        self.quality_points = float(quality_points)
        self.gpa = self.quality_points / self.hours
        Student.student_counter += 1
        Student.all_students.append(self)
        Student.top_student = Student.best_student()

    @classmethod
    def best_student(cls):
        """
        Take all_students as input and return the student with the
        best GPA.
        :return: object
        """
        top_student = cls.all_students[0]
        for student in cls.all_students:
            if student.gpa > top_student.gpa:
                top_student = student
        return top_student

    @classmethod
    def create_students(cls, filename):
        """
        Read file and create student objects.
        :param filename: string
        """
        Student_info = namedtuple('Student_info',
                                  'last_name first_name hours q_points')
        with open(filename, mode='r') as f:
            for line in f:
                line = Student_info(*line.split())
                full_name = str(line.first_name).capitalize() + ' ' + str(line.last_name).capitalize()
                cls(full_name, line.hours, line.q_points)

    @classmethod
    def print_results(cls):
        """
        Take the student with the highest GPA and print their report.
        Print the report of the best student.
        """
        assert isinstance(cls.top_student, cls)
        string = cls.top_student.name, cls.top_student.hours, cls.top_student.gpa
        print('The best student is {0} who has spent {1} hours and has a {2} gpa.'.format(*string))


def main():
    Student.create_students('students.txt')  # creates student objects
    Student.print_results()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
