"""
תרגיל 1
"""


def rerturn_just_adult_active_list(all_people_list):         
    just_name_of_adult_and_active_list = []
    for person in all_people_list:
        if person[1] >= 18 and person[2] == "active":
            just_name_of_adult_and_active_list.append(person[0])
    return just_name_of_adult_and_active_list

all_people_list = [
    ["Dan", 25, "active"],
    ["Noa", 16, "active"],
    ["Yael", 30, "inactive"],
]

print(rerturn_just_adult_active_list(all_people_list))


def f(l):
    r = []
    for x in l:
        if x[1] >= 18 and x[2] == "active":
            r.append(x[0])
    return r

d = [
    ["Dan", 25, "active"],
    ["Noa", 16, "active"],
    ["Yael", 30, "inactive"],
]

print(f(d))



"""
תרגיל 2
"""

def handle_purchase(user_email, product_name, product_price, stock, quantity):
    if not user_email:
        print("Invalid user")
        return None
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return None

    price = product_price * quantity
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85

    stock -= quantity

    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = price
    order_status = "confirmed"
    print(f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}")
    return order_user, order_product, order_quantity, order_total, order_status




def handle_purchase(user_email, product_name, product_price, stock, quantity):
    if check_email(user_email) == False:
        return None
        
    if check_quantity(stock, quantity) == None:
        return None

    price = price_calc(product_price, quantity)

    stock -= quantity

    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = price
    order_status = "confirmed"
    print(f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}")
    return order_user, order_product, order_quantity, order_total, order_status



def check_email(user_email):
    if len(user_email) == 0:
        return False
    else:
        return True
    
def check_quantity(stock, quantity):
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return None
        


def price_calc(product_price, quantity):
    price = product_price * quantity
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85

    return price


"""
תרגיל 3
"""

def manage_students(names, grades, new_name, new_grade):
    # validation
    if not new_name or len(new_name) < 2:
        print("Error: invalid name")
        return students
    if new_grade < 0 or new_grade > 100:
        print("Error: grade must be 0-100")
        return students

    # add student
    grades.append(new_grade)

    # calculate stats
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)

    # print report
    print("=== Student Report ===")
    for i in range(len(names)):
        print(f"  {names[i]}: {grades[i]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")

    # save to file
    with open("students.txt", "w") as f:
        for i in range(len(names)):
            f.write(f"{names[i]},{grades[i]}\n")

    return names, grades


def manage_students(names, grades, new_name, new_grade):
    if(valid(new_name, new_grade)):
        grades.append(new_grade)

        average, top_count, failing_count = calc_avg_and_top_count_and_failing_count(grades)

        print_grades_and_count_of_top_failing(average, top_count, failing_count, names, grades)

        save_to_file(names, grades)

        return names, grades


def valid(new_name, new_grade):
    if not new_name or len(new_name) < 2:
        print("Error: invalid name")
        return False
    if new_grade < 0 or new_grade > 100:
        print("Error: grade must be 0-100")
        return False
    return True

def calc_avg_and_top_count_and_failing_count(grades):
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)

    return average, top_count, failing_count

def print_grades_and_count_of_top_failing(average, top_count, failing_count, names, grades):
        print("=== Student Report ===")
        for i in range(len(names)):
            print(f"  {names[i]}: {grades[i]}")
        print(f"Average: {average:.1f}")
        print(f"Top students: {top_count}")
        print(f"Failing: {failing_count}")

def save_to_file(names, grades):
    with open("students.txt", "w") as f:
        for i in range(len(names)):
            f.write(f"{names[i]},{grades[i]}\n")


"""
תרגיל 4
"""

#  ישן

def create_admin_user(name, email):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")
    return name, email, "admin", "2024-01-01", True
    

def create_editor_user(name, email):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")
    return name, email, "editor", "2024-01-01", True
    

def create_viewer_user(name, email):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")
    return name, email, "viewer", "2024-01-01", True

#חדש


def valid(name, email):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")
    
def create_user(name, email, tafkid):
    valid(name, email)
    return name, email, tafkid, "2024-01-01", True


"""
תרגיל 5
"""

def get_status(score):
    if score >= 90:
        status = "excellent"
    elif 70 <= score < 90:
        status = "good"
    elif  55 <= score < 70:
        status = "average"
    elif score < 55:
        status = "fail"
    else:
        status = "unknown"
    return status


def is_valid_age(age):
    if isinstance(age, int):
        if 0 <= age <= 120:
            return True
        else:
            return False


def get_greeting(hour):
    greeting = ''
    if 5 <= hour < 12:
        greeting = "Good morning"
    if 12 <= hour < 17:
        greeting = "Good afternoon"
    if 17 <= hour < 21:
        greeting = "Good evening"
    if 21 <= hour < 5:
        greeting = "Good night"
    return greeting


"""
תרגיל 6
"""

def process_grades(names, all_grades):
    result_names = []
    result_averages = []
    result_statuses = []
    result_highs = []
    result_lows = []
    for i in range(len(names)):
        name = names[i]
        grades = all_grades[i]

        if not name:
            print(f"Error: missing name")
            continue
        if not grades:
            print(f"Error: {name} has no grades")
            continue

        total = sum(grades)
        average = total / len(grades)
        status = "pass" if average >= 56 else "fail"
        highest = max(grades)
        lowest = min(grades)

        result_names.append(name)
        result_averages.append(round(average, 1))
        result_statuses.append(status)
        result_highs.append(highest)
        result_lows.append(lowest)
    
    
    
    
    

    print("=" * 40)
    print("Student Grade Report")
    print("=" * 40)
    for i in range(len(result_names)):
        print(f"Name: {result_names[i]}")
        print(f"  Average: {result_averages[i]}")
        print(f"  Status: {result_statuses[i]}")
        print(f"  Range: {result_lows[i]} - {result_highs[i]}")
        print()

    passing_count = sum(1 for s in result_statuses if s == "pass")
    print(f"Total passing: {passing_count}/{len(result_names)}")
    return result_names, result_averages, result_statuses


def valid 
    
