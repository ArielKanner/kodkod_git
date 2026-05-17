"""
תרגיל 1
"""
def sum_list(list):
    sum = 0
    for n in list:
        sum += n
    return sum

"""
תרגיל 2
"""
def max_element(my_list):
    mx = my_list[0]
    for n in my_list:
        if n > mx:
            mx = n
    return mx

"""
תרגיל 3
"""

def amont_in_list(my_list, value):
    count = 0
    for val in my_list:
        if val == value:
            count+=1
    return count

"""
תרגיל 4
"""

def rvrs_list(my_list):
    res_l = []
    for i in range((len(my_list)-1), -1, -1):
        res_l.append(my_list[i])
    return res_l


"""
תרגיל 5
"""

def remove_duplicates(my_list):
    new_list = []
    for element in my_list:
        if element not in new_list:
            new_list.append(element)
    return new_list

"""
 תרגיל 6
"""
def second_max(my_list):
    my_max = max(my_list)
    my_second = None

    for num in my_list:
        if num < my_max:
            if my_second == None:
                my_second = num
            elif num > my_second:
                my_second = num
    return my_second

"""
תרגיל 7
"""
def merge_two_sorted_lists(list_1, list_2):
    list_3 = []
    index_1 = 0
    index_2 = 0

    while index_1 < len(list_1) and index_1 < len(list_2):
        if list_1[index_1] <= list_2[index_2]:
            list_3.append(list_1[index_1])
            index_1 += 1
        else:
            list_3.append(list_2[index_2])
            index_2 += 1
    list_3.extend(list_1[index_1:])
    list_3.extend(list_2[index_2:])

    return list_3


"""
תרגיל 8
"""
def rotate_a_list(my_list, k):
    new_list = []
    k = k % len(my_list)
    for i in range((len(my_list)- k), len(my_list)):
        new_list.append(my_list[i])
    for i in range(len(my_list)- k):
        new_list.append(my_list[i])
    return new_list
print(rotate_a_list([1,2,3,4], 7))
    

