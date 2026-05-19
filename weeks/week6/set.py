def remove_duplicates(my_list):
    return list(set(my_list))

"""
תרגיל 2
"""
def count_unique_elements(my_list):
    my_set =  set(my_list)
    count =0 
    for element in my_set:
        count+=1
    return count
#print(count_unique_elements([1, 2, 2, 3, 1, 4]))

"""
תרגיל 3
"""

def common_elements(list_1, list_2):
    res_set = set(list_1).intersection(set(list_2))
    return list(res_set)
#print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))

"""
תרגיל 4
"""

def elements_in_only_one(list_1, list_2):
    res_set = set(list_1).symmetric_difference(set(list_2))
    return list(res_set)
#print(elements_in_only_one([1, 2, 3, 4], [3, 4, 5, 6])) 

"""
תרגיל 5
"""
def is_subset(list_a, list_b):
    union_set = set(list_a).union(set(list_b))
    return set(list_b) == union_set
#print(is_subset( [1, 2, 3], [1, 2, 3, 4, 5]))

"""
תרגיל 6
"""

def unique_characters(my_string):
    string_list = list(my_string)
    set_string = set(set_string)
    return list(set_string) == string_list

"""
תרגיל 7
"""
def first_repeated_element(my_list):
    my_set = set(my_list)
    for element in my_list:
        if element in my_set:
            my_set.remove(element)
        else:
            return element
    return None

#print(first_repeated_element( [1, 2, 3, 4]))

"""
תרגיל 8
"""
def distinct_words(my_string):
    my_string = my_string.lower()
    my_set = set(my_string.split(" "))
    return len(my_set)
#print(distinct_words("The cat and the dog and the bird"))

"""
תרגיל 9
"""
def pair_sum_exists(num_list, target):
    my_set = set(num_list)
    for element in my_set:
        if (target-element) in my_set:
            return True
    return False

#print(pair_sum_exists([3, 1, 4, 7, 2], 11))