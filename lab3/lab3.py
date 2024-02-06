
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
                    print(word)
                    if word in table:
                        if line_number not in table[word]:
                            table[word].append(line_number)
                    else:
                        table[word] = [line_number]

        return table
        
    except IOError:
        print("Error opening " + filename)
    

def main():
    print(index_text("summer.txt"))

if __name__ == '__main__':
    main()