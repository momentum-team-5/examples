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


def join_collection(coll, sep=" "):
    """
    Convert elements of coll to a string and join with sep.
    """
    output_items_as_str = []

    for item in coll:
        output_items_as_str.append(str(item))

    return sep.join(output_items_as_str)


def save_results_in_csv(fname, row):
    """
    Append a row to a CSV file.
    """
    row_as_strings = join_collection(row, sep=";")
    
    with open(fname, "at+") as csv:
        csv.write(row_as_strings)
        csv.write('\n')


def show_csv(fname):
    """
    Pretty-print the data in a CSV file.
    """

    with open(fname, "rt") as csv:
        csv_iter = iter(csv)
        next(csv_iter)
        
        for row in csv_iter:
            pretty_row = row.strip().replace(";", ",  ")
            print(pretty_row)
