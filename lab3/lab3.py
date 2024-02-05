
def insert_in_sorted(x: int, sorted_list: list):
    for i in range(len(sorted_list)):
        if sorted_list[i] >= x:
            sorted_list.insert(i, x)
            break

    else:
        sorted_list.append(x)

    return sorted_list

def main():
    print(insert_in_sorted(2,[2,2]))

if __name__ == '__main__':
    main()