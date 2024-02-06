# -*- coding: utf-8 -*-

import lab3 as l3

test_dict = {"hej": [5, 15, 27],
             "din": [6],
             "brax": [6],
             "spenat": [6, 5, 77, 11],
             "filur": [4,5],
             "minsann": [4, 5]}

my_list = l3.important_words(test_dict, ["din"])
print("My list: {}".format(my_list))
sorted_list = l3.insertion_sort(my_list)
assert len(sorted_list) == 5
print(sorted_list)
assert sorted_list[0][0] == "spenat"
assert sorted_list[1][0] == "hej"
assert sorted_list[4][0] == "brax"

