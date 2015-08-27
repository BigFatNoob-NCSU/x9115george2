from __future__ import print_function

__author__ = 'panzer'


class Employee:
    """
    Class Employee.
    Contains auto incremented employee id,
    employee's name and age.
    """
    id = 0

    def __init__(self, name, age):
        """
        Initialize an employee with name and age. Auto increment id
        :param name: Name of the employee
        :param age: Age of the employee
        :return:
        """
        Employee.id += 1
        self.id = Employee.id
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return """
        ** Employee #{} **
        Name : {}\
        Age  : {}
        """.format(self.id, self.name, self.age)


if __name__ == "__main__":
    employees = [
        Employee("George", 4),
        Employee("Vivek", 6),
        Employee("Rahul", 3),
        Employee("Wei", 6),
        Employee("Tim", 10)]
    print(sorted(employees))
