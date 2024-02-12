"""LAB 4"""

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
        filename = input('Which csv file should be analyzed? ')
        if os.path.exists(filename):
            break

    return filename

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
            average = x_sum/n
        print(batch, "\t", average)

def read_data(filename: str) -> dict:
    """Reading and collecting data from a file

    Args:
        filename (str): The file which contains the data to be read.

    Returns:
        dict: The data is collected and stored in this dictionary
    """

    data = {}
    with open(filename, 'r', encoding="utf-8") as h:
        for line in h:
            four_vals = line.split(',')
            batch = four_vals[0]
            if not batch in data:
                data[batch] = []
            # Collect data from an expe friment:
            data[batch] += [(float(four_vals[1]), float(four_vals[2]), float(four_vals[3]))]

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
