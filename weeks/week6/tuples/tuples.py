import math

def sum_of_tuple(my_tuple):
    my_sum = 0
    for num in my_tuple:
        my_sum+=num
    return my_sum

"""
תרגיל 2
"""
def max_in_tuple(my_tuple):
    my_max = my_tuple[0]
    for num in my_tuple:
        if num > my_max:
            my_max = num
    return my_max

#print(max_in_tuple((1,2,4,3)))

"""
תרגיל 3
"""
def count_occurences(my_tuple, value):
    count = 0
    for element in my_tuple:
        if element == value:
            count += 1
    return count

"""
תרגיל 4
"""
def reverse_tuple(my_tuple):
    rvrs_list = []
    for i in range(len(my_tuple)-1, -1, -1):
        rvrs_list.append(my_tuple[i])
    new_tuple = tuple(rvrs_list)
    return new_tuple
#print(reverse_tuple((1,2,3,'hi',-4)))

"""
תרגייל 5
"""

def swap_pairs(my_tuple):
    swap_list = []
    for i in range(0, len(my_tuple), 2):
        swap_list.append(my_tuple[i+1])
        swap_list.append(my_tuple[i])
    swap_tuple = tuple(swap_list)
    return swap_tuple
#print(swap_pairs((2,1,4,3,6,5)))

"""
תרגיל 6
"""

def min_and_max(my_tuple):
    my_min = my_tuple[0]
    my_max = my_tuple[0]
    for num in my_tuple:
        if my_tuple[i] > my_max:
            my_max = my_tuple[i]
        if my_tuple[i] < my_min:
            my_min = my_tuple[i]
    return my_max, my_min

"""
תרגיל 7
"""

def distance(first_point, second_point):
    dstnc = math.sqrt(math.pow((second_point[1]-first_point[1]), 2) + math.pow((second_point[0]-first_point[0]), 2))
    return dstnc

"""
תתרגיל 8
"""

def merge_and_sort(tuple_1, tuple_2):
    merge_list = []
    merge_list.extend(list(tuple_1))
    merge_list.extend(list(tuple_2))

    for i in range(0, len(merge_list)-1):
        for k in range(i+1, len(merge_list)):
            if merge_list[i]>merge_list[k]:
                merge_list[i], merge_list[k] = merge_list[k], merge_list[i]
    return tuple(merge_list)

#print(merge_and_sort((1,3,-2), (-4,0,1)))

"""
תרגיל 9
"""

def frequency_table(my_tuple):
    res_list = []
    check_list = []
    
    for element in my_tuple:
        if element not in check_list:
            check_list.append(element)
            res_list.append((element, my_tuple.count(element)))

    return tuple(res_list)

#print(frequency_table(('a','b','a','c','b','a',1,1)))


"""
תרגיל 10
"""
def rotate_tuple(my_tuple, k):
    rotate_list = []


    k = k % len(my_tuple)
    for i in range((len(my_tuple)- k), len(my_tuple)):
        rotate_list.append(my_tuple[i])
    for i in range(len(my_tuple)- k):
        rotate_list.append(my_tuple[i])

    return tuple(rotate_list)

#print(rotate_tuple([1,2,3,4], 7))
