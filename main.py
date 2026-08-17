"""Sortiere Studenten nach Noten.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu04/aufgaben/sorting2
"""

def sort_students_by_grade(students):
    """
    Nutze die `sorted()` Funktion, um die Studenten basierend auf ihren Noten zu sortieren.

    Parameters:
    - students (list): Liste der Studenten und ihrer Noten.

    Returns:
    - list: Liste der sortierten Studenten.
    """
    return []


if __name__ == '__main__':
    students = [
        ('Alice', 4.0),
        ('Bob', 3.5),
        ('Charlie', 4.25),
        ('David', 5.5),
        ('Manuel', 3.75),
    ]
    sorted_students = sort_students_by_grade(students)
    print(sorted_students)
