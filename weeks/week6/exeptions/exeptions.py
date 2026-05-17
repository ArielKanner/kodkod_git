"""
תרגיל 1
"""
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None
print(safe_int(34))

"""
תרגיל 2
"""

def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "undefind"
    except TypeError:
        return "undefind"
    
"""
תרגיל 3
"""
def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return "missing"
    
"""
תרגיל 4
"""

def parsr_ints(values):
    new_list = []
    for val in values:
        try:
            new_list.append(int(val))
        except ValueError:
            pass
    return new_list

print(parsr_ints([1,3,'r','t',4]))

"""
תרגיל 5
"""

# def set_age(age):
#     if age > 150 or age


"""
תרגיל 6
"""
def retry(func, n):
    error = None
    for i in range(n):
        try:
            return func()
        except Exception as e:
            error = e
    raise error

"""
תרגיל 7
"""

def count_errors(funcs):
    count = 0
    for func in funcs:
        try:
            func()
        except:
            count += 1
    return count


"""
תרגיל 8
"""

def load_config(path):
    with open(path, 'r', encoding='UTF-8') as f1:
        try:
            return int(f1.readline())
        except Exception:
            raise RuntimeError("failed to load config")
        

print(load_config('a_file.txt'))