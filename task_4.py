from accepts import accepts


class Student:
    """
    The class represents a student by its name, id number and grades.
    """
    def __init__(self, name: str, id_number: str):
        """
        The init function constructs the student's object and receives its name and id number.
        :param name: The student's name.
        :param id_number:The student's id number.
        """
        self.name = name
        self.id_number = id_number
        self.grades = []

    @property
    def name(self) -> str:
        """
        The function returns the student's name.
        :return: The student's name.
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        The function sets the student's name with the name it gets.
        :param value: The student's name.
        :return: None.
        """
        self._name = value

    def add_grade(self, grade: int) -> None:
        """
        The function gets a grade and adds it to the student's grade list.
        :param grade: The student's name to be added to the student's grade list.
        :return: None.
        """
        self.grades.append(grade)


@accepts(int)
def calculate_grade(reduction: int) -> int:
    """
    The function calculates a grade by subtracting the points it receives from 100.
    :param reduction: The points to be subtracted.
    :return: The calculated grade.
    """
    return 100 - reduction


if __name__ == '__main__':
    student = Student("Lee Levi", "208926402")
    print(student.name)
    student.name = "Lee Kol Levi"
    print(student.name)
    student.add_grade(calculate_grade(4))
