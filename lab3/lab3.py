# -*- coding: utf-8 -*-

def insert_in_sorted(x, sorted_list: list):
    for i, item in enumerate(sorted_list):
        if type(x) is tuple: ## Diffrent comparison being made if x is tuple or not
            if len(x[1]) > len(item[1]): ## Taking in a tuple and comparing the lenghts of the arrays (Number of occurences)
                sorted_list.insert(i, x)
                break
        else:
            if sorted_list[i] > x:
                sorted_list.insert(i, x)
                break

    else:
        sorted_list.append(x)

    return sorted_list


def insertion_sort(my_list: list):
    out: list = []
    for x in my_list:
        out = insert_in_sorted(x, out)

    return out

def number_lines(f: str):
    try:
        with open(f, "r") as file:
            try:
                with open(f"numbered_{f}", "w") as new_file:
                    for index, line in enumerate(file):
                        new_file.write(f"{index} {line}")

            except IOError:
                print("Error creating new file!")

    except IOError:
        print("File not found! " + f)

def index_text(filename: str):
    table: dict = {}
    try:
        with open(f"./{filename}", "r") as file:
            for line_number, line in enumerate(file):
                for word in line.lower().replace("\n", "").split(" "): # Set all lower case letters, removing new lines and splitting the line into words
                    if word in table:
                        if line_number not in table[word]:
                            table[word].append(line_number)
                    else:
                        table[word] = [line_number]

        return table
        
    except IOError:
        print(f"File '{filename}' not found!")

def important_words(an_index: dict, stop_words: list):

    an_index_no_stop_words = [(word, an_index[word]) for word in an_index if word not in stop_words] # Removes the stop words from the dict

    sorted_list = insertion_sort(an_index_no_stop_words)
    important_words: list = [word[0] for word in sorted_list[:5]]
    
    return important_words

def user_filename_input():
    current_stop_words = ["and", "I", "that", "it", "for"]  # English/Swedish stop words ["jag", "gör", "och", "så", "det"]

    while True:

        file_choice = str(input("Enter a text file: "))
        indexed_text = index_text(file_choice)

        if indexed_text:
            break

    result = important_words(indexed_text, current_stop_words)

    print("The most important words are: ")
    for word in result:
        print(word)

def main():
    user_filename_input()

if __name__ == '__main__':
    main()