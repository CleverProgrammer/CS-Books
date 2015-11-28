"""
Author: Rafeh Qazi
Create a student class that models a student.
Date: 11/27/2015
"""


class Student:
    """
    A student class that models a student.

    >>> qazi = Student(name='rafeh', hours=40, quality_points=100)
    >>> qazi.name
    'rafeh'
    >>> qazi.hours
    40.0
    >>> qazi.quality_points
    100.0
    >>> qazi.gpa()
    2.5
    >>> nick = Student('drane', 20, 100)
    >>> nick.gpa()
    5.0
    >>> rafeh = Student.make_student('Qazi, Rafeh   40  100')
    >>> rafeh.name
    'Qazi, Rafeh'
    """

    def __init__(self, name, hours, quality_points):
        self.name = name
        self.hours = float(hours)
        self.quality_points = float(quality_points)

    def gpa(self):
        """
        Return the gpa of a student.
        :return: float.
        """
        return self.quality_points / self.hours

    @staticmethod
    def make_student(info_string):
        """
        info_string is a tab-separated line: name hours qpoints.
        :param info_string: str
        :return: object
        """
        last, first, hours, quality_points = info_string.split()
        name = str(last) + ' ' + str(first)
        return Student(name, hours, quality_points)


def main():
    filename = input('Enter the name of the grade file: ')
    with open(filename, 'r') as f:
        best_student = Student.make_student(f.readline())
        for line in f:
            student = Student.make_student(line)
            if student.gpa() > best_student.gpa():
                best_student = student
    print('The best student is:', best_student.name)
    print('hours:', best_student.hours)
    print('GPA:', best_student.gpa())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
