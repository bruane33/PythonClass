"""
Program: Student Class with tests

Author: Brian Ruane

Last date modified: 06/28/2022

The purpose of this program is demonstrate the use unit testing with classes
"""

from class_definitions.student import Student

student1 = Student("McCheese", "Mayor", "Political Science", 3.4)
student2 = Student("Burgler", "Ham", "Finance", 2.2)

print(str(student1))
print(str(student2))

del student1
del student2
