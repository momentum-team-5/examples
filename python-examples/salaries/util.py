import os


def validate_input_is_float(prompt, error):
    """
    Loop until the user supplies a value that can be interpreted as a floating point number.
    """
    valid_input_flag = False

    while not valid_input_flag:
        user_input = input(prompt)

        try:
            output = float(user_input)

        except ValueError:
            print(error)

        else:
            valid_input_flag = True

    return output


def calculate_pay(hours_worked, hourly_rate):
    """
    Determine the total pay owed, accounting for overtime.
    """
    regular_hours = min(40, hours_worked)
    overtime_hours = max(0, hours_worked - 40)
    overtime_rate = hourly_rate * 1.5

    return regular_hours * hourly_rate + overtime_hours * overtime_rate


def save_results_in_csv(fname, row):
    """
    Append a row to a CSV file.
    """
    pass
