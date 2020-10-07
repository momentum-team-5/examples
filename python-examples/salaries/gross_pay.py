#!/usr/local/bin/python3

from util import calculate_pay, validate_input_is_float, save_results_in_csv, show_csv


CSV_FILE = "employee-pay.csv"


def main(argv):
    """
    Main application logic.
    """
    if "-p" in argv or "--print" in argv:
        show_csv(CSV_FILE)
        return

    employee_name = input("Enter the employee's name: ")
    hours_worked = validate_input_is_float("Enter number of hours worked: ", "Hours worked must be a number.")
    hourly_rate = validate_input_is_float("Enter hourly rate: ", "Hourly rate must be a number.")
    employee_pay = calculate_pay(hours_worked, hourly_rate)

    if "-v" in argv or "--verbose" in argv:
        print(f"Total: ${employee_pay:,.2f}")

    if "-s" in argv or "--safe" in argv:
        save_results_in_csv(CSV_FILE, [employee_name, hours_worked, hourly_rate, employee_pay])


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
