"""LAB 4
The goal of this program is to read in a data file with (invented) data from several batches of measurements,
taken from different points on the plane, and for each batch calculate the average of the measurements
taken inside the unit circle. A point (𝑥, 𝑦) in the plane is inside the unit circle if 𝑥2 + 𝑦2 ≤ 1.
Measurements taken outside the unit circle should be ignored. The data file has four columns separated
with commas: it is a so-called csv file (where “csv” stands for comma-separated values). The first number
records which batch a measurement belongs to, while the second and third record the 𝑥- and𝑦-coordinates
where the measurement was taken, and the fourth number is the measurement itself.
"""

import os

# Sample data:
# 1, 0.1, 0.2, 73
# 1, 0.11, 0.1, 101
# 2, 0.23, -0.01, 17
# 2, 0.9, 0.82, 23
#
# Pretend this is taken from two (or more) different experiments:
# batch 1 and batch 2.

def get_user_file_choice() -> str:
    """
    Get user input from in which checks if the desired file exists.
    User stuck here util a valid file is entered.
    """
    while True:
        filename = input('Which csv file should be analyzed?: ')
        if os.path.exists(filename):
            return filename
        print(f'File "{filename}" not found!')


def print_and_process_results(data: dict):
    """Prints the results after it being processed.

    Args:
        data (dict): The dictionary in which the results are stored
    """
    print("Batch\t Average")
    for batch, sample in data.items():
        n = 0
        x_sum = 0
        for (x, y, val) in sample:
            if x**2 + y**2 <= 1:
                x_sum += val
                n += 1
            try:
                average = x_sum/n
                print(batch, "\t", average)

            except ZeroDivisionError: # Catches error if trying to divide by zero
                print(batch, "\t", "Can not divide by zero. Averge is not possible!")


def read_data(filename: str) -> dict:
    """Reading and collecting data from a file

    Args:
        filename (str): The file which contains the data to be read.

    Returns:
        dict: The data is collected and stored in this dictionary
    """

    data = {}
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            four_vals = line.strip().split(',')
            if four_vals == [""]:
                break
            batch = four_vals[0]
            if not batch in data:
                data[batch] = []
            # Collect data from an expe friment:
            try:
                data[batch] += [(float(four_vals[1]), float(four_vals[2]), float(four_vals[3]))]
            except ValueError:
                print(f"{four_vals} ignored - Not valid input!")

    return data

def main():
    '''
    This is the main body of the program.
    '''

    filename = get_user_file_choice()
    data = read_data(filename)
    print_and_process_results(data)


# Start the main program: this is idiomatic python
if __name__ == '__main__':
    main()

# The idea with this idiom is that if this code is loaded as a module,
# then the __name__ variable (internal to Python) is not __main__ and
# the body of the program is not executed. Consider what would happen
# if the main function was not in a function: an import statement (for
# example "import o4") would load the functions and then executed
# "filename = input(...)" and that is probably not what you want. The
# idiom is simply an easy way of ensuring that some code is only
# executed when run as an actual program.
#
# Try it out by importing this file into another project!
