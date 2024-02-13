"""
LAB 4

The goal of this program is to read in a data file with (invented) data from 
several batches of measurements, taken from different points on the plane,
and for each batch calculate the average of the measurements taken inside the unit circle.
A point (x, y) in the plane is inside the unit circle if x^2 + y^2 ≤ 1.

Measurements taken outside the unit circle should be ignored.
The data file has four columns separated with commas: it is a so-called csv file
(where “csv” stands for comma-separated values). The first number records which batch a measurement
belongs to, while the second and third record the x- and y-coordinates
where the measurement was taken, and the fourth number is the measurement itself.
"""
import math
import os

import matplotlib.pyplot as plt

# Sample data:
# 1, 0.1, 0.2, 73
# 1, 0.11, 0.1, 101
# 2, 0.23, -0.01, 17
# 2, 0.9, 0.82, 23
#
# Pretend this is taken from two (or more) different experiments:
# batch 1 and batch 2.

def get_user_file_choice() -> str:
    """ Get user input from in which checks if the desired file exists.
        User stuck here until a valid file is entered.
    """
    while True:
        filename = input('Which csv file should be analyzed?: ')
        print()
        if os.path.exists(filename):
            return filename
        print(f'File "{filename}" not found!')


def print_results(results: dict):
    """Firstly sorts the batches and prints the averges from each.

    Args:
        results (dict): Dictonay containg the batch respectively the averge
    """
    soreted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    print("Batch\t Average")
    for batch, average in soreted_results:
        print(batch, "\t", average)


def process_data(data: dict) -> dict:
    """Process the data by calculating each batch and ignoring those with values is greater than 1.

    Args:
        data (dict): The dictionary in which the results are stored
    """
    processed_data = {}
    for batch, sample in data.items():
        n = 0
        x_sum = 0
        for (x, y, val) in sample:
            if x**2 + y**2 <= 1:
                x_sum += val
                n += 1
            try:
                average = x_sum/n
                processed_data[batch] = average

            except ZeroDivisionError: # If value is over 1 then it will try to divide by zero.
                pass

    return processed_data

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
                print(f"Warning: wrong input format for entry: {four_vals}\n")

    return data

def plot_data(data: dict ,f: str):
    """Plots out the data a displays it in realtion to a circle and a graph.

    Args:
        data (dict): The data to be displayed
        f (str): filename to be rendered with.
    """
    filename = f.replace(".csv", ".pdf")
    # Calculate 150 coordinates to draw the circle
    angles = [ n/150 * 2 * math.pi for n in range(151) ]
    x_coords = [ math.cos(a) for a in angles ]
    y_coords = [ math.sin(a) for a in angles ]
    # Draw the circle
    plt.plot(x_coords,y_coords)

    colors = ['r', 'b', 'g', 'c', 'm']
    colors_index = 0
    offset = 0.02

    # Here be your code to plot "data"
    for batch in data:
        for x, y, measurement in data[batch]:
            plt.plot(x,y, colors[colors_index]+"o", markersize=3.5)
            plt.text(x + offset, y + offset, measurement, fontsize=5, ha='left', color=colors[colors_index])
        colors_index += 1

    plt.savefig(filename)
    print("\nA plot of data can be found in " + filename)



def main():
    '''
    This is the main body of the program.
    '''

    filename = get_user_file_choice()
    data = read_data(filename)
    result = process_data(data)
    print_results(result)
    plot_data(data, filename)


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
