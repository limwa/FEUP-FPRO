def get_average_grade(record):
    _, _, grades = record
    return sum(grades) / len(grades)

def sort_grades(records):
    return tuple(sorted(sorted(sorted(records, key=lambda x: x[1]), key=lambda x: x[0]), key=get_average_grade, reverse=True))
