def sum_of_val(my_dict):
    sum = 0
    for v in my_dict.values():
        sum += v

"""
תרגיל 2
"""
def sum_of_val(my_dict):
    max_val = max(my_dict.values())
    for i in my_dict():
        if my_dict[i] == max_val:
            return i
        
"""
תרגיל 3
"""

def count_chars(my_string):
    my_dict = {}
    for c in my_string:
        if c not in my_dict:
            my_dict[c] = 1
        else:
            my_dict[c] += 1
    return my_dict

#print(count_chars('banana'))

"""
תרגיל 4
"""

def invert_dict(my_dict):
    invert_dict = {}
    for k, v in my_dict.items():
        invert_dict[v] = k
    return invert_dict
#print(invert_dict({'a':1,'b':3, 'hi': 'what'}))

"""
תרגיל 5
"""

def merge_dicts(first_dict, second_dict):
    merge_dict = {}
    merge_dict.update(first_dict)
    merge_dict.update(second_dict)
    return merge_dict

#print(merge_dicts({1:1,2:20}, {2:30, 3:40}))

"""
תרגיל 6
"""

def filter_by_value(my_dict, val):
    filtered_dict = {}
    for k, v in my_dict.items():
        if v > val:
            filtered_dict[k] = v
    return filtered_dict
#print(filter_by_value({'a':1,'b':30, 'c': 40 , 'd': 10}, 15))


"""
תרגיל 7
"""

def group_by_first_letter(my_list):
    res_dict = {}
    for element in my_list:
        if element[0] not in res_dict:
            res_dict[element[0]] = [element]
        else:
            res_dict[element[0]].append(element)
    return res_dict
#print(group_by_first_letter(['ar', 'as', 'bb', 'cc', 'cf']))


"""
תרגיל 8
"""

def word_frequency(my_string):
    my_dict = {}
    my_list = my_string.split(" ")
    
    for word in my_list:
        if word not in my_dict:
            my_dict[word] = 1
        else:
            my_dict[word] +=1
    return my_dict
#print(word_frequency("the cat sat on the mat on the mat"))

"""
תרגיל 9
"""

def common_keys(dict_1, dict_2):
    res_list = []
    dict_3 = {}
    
    dict_3.update(dict_1)
    dict_3.update(dict_2)
    for k in dict_3:
        if k in dict_1 and k in dict_2:
                res_list.append(k)
    return res_list

#print(common_keys({"a": 1, "b": 2, "c": 3}, {"b": 9, "c": 8, "d": 7}))

"""
תרגיל 10
"""
def most_val(my_dict):
    count_val_dict = {}
    for v in my_dict.values():
        if v not in count_val_dict:
            count_val_dict[v] = 1
        else:
            count_val_dict[v] += 1
    most_val = max(count_val_dict)

    for k, v in count_val_dict.items():
        if v == most_val:
            return k

print(most_val({"a": 1, "b": 2, "c": 1, "d": 3, "e": 1}))
