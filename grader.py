def calculate_total_and_percentage(marks_dict):
    total_marks = sum(marks_dict.values())
    number_of_subjects = len(marks_dict)
    percentage = total_marks / number_of_subjects
    return total_marks, percentage


def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 35:
        return "D"
    else:
        return "Fail"
