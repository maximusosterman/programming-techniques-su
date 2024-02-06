# -*- coding: utf-8 -*-

def insert_in_sorted(x: int, sorted_list: list):
    for i in range(len(sorted_list)):
        if sorted_list[i] > x:
            sorted_list.insert(i, x)
            break

    else:
        sorted_list.append(x)

    return sorted_list


def insertion_sort(my_list: list):
    out: list = []
    for x in my_list:
        insert_in_sorted(x, out)

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
        with open(filename, "r") as file:
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
    important_words_list: list = []

    an_index_no_stop_words = [(word, an_index[word]) for word in an_index if word not in stop_words] # Removes the stop words from the dict

    list

    # important_words_list = important_words_list[:5] # The five most important words
    
    return an_index_no_stop_words
    
    

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
    # debugging(index_text("idas.txt"))
    my_list = important_words(index_text("idas.txt"), ["jag", "göt", "och", "så", "det"])
    # sorted_list = insertion_sort(my_list)

    # print(sorted_list)


    # test_dict = {"hej": [5, 15, 27],
    #          "din": [6],
    #          "filur": [4,5],
    #          "minsann": [4, 5]}

    # my_list = important_words(test_dict, ["din"])

    # sorted_list = insertion_sort(my_list)
    # print(sorted_list)

if __name__ == '__main__':
    main()