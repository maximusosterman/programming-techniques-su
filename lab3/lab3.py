# -*- coding: utf-8 -*-

def insert_in_sorted(x, sorted_list: list):
    print("insert_in_sorted {} {}".format(x, sorted_list))
    for i, item in enumerate(sorted_list):
        print("X: {} Item: {}".format(x, item))
        if len(x[1]) > len(item[1]):

            print("len(x[1]) > len(item[i][1]) - {} > {} - Inserted in position {}".format(len(x[1]), len(item[1]), i))
            sorted_list.insert(i, x)
            break
    else:
        sorted_list.append(x)

    return sorted_list


def insertion_sort(my_list: list):
    print("Insersion sort {}".format(my_list))
    out: list = []
    for x in my_list:
        print("Handling {}".format(x))
        out = insert_in_sorted(x, out)
        print("OUT: {}".format(out))

    return out

def number_lines(f: str):
    try:
        with open(f, "r") as file:
            try:
                with open(f"numbered_{f}", "w") as new_file:
                    for index, line in enumerate(file):
                        new_file.write(f"{index} {line}")

            except IOError:
                print("Error creating new file")

    except IOError:
        print("Error opening " + f)

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
        print("Error opening " + filename)

def important_words(an_index: dict, stop_words: list):

    an_index_no_stop_words = [(word, an_index[word]) for word in an_index if word not in stop_words] # Removes the stop words from the dict
    
    return an_index_no_stop_words[5:]

def user_filename_input():
    file_choice = str(input("Enter a text file: "))
    current_stop_words = ["and", "I", "that", "it", "for"]

    result = index_text(file_choice)

    # result = important_words(index_text(file_choice), current_stop_words)
    if result:
        print("The most important words are: ")
        for word in result:
            print(word)

    

def debugging(my_dict):
    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: len(x[1])))
    for word in sorted_dict:
        print(f"{word}, {len(sorted_dict[word])}")

def main():
    idas_dict = index_text("idas.txt")
    my_list = important_words(idas_dict, ["jag", "gör", "och", "så", "det"])
    sorted_list = insertion_sort(my_list)
    print(sorted_list)
    

if __name__ == '__main__':
    main()