with open('diary.txt', 'w') as f:
    f.write("hi\n")
    f.write("i am\n")
    f.write("ariel\n")    
print("יומן נוצר בהצלחה")

with open('diary.txt', "r") as f:
    diary = f.read()

print(diary)


def add_write(file_name, content):
    with open(file_name, 'a') as f:
        f.write(content)

add_write('diary.txt', "wow")


def search_diary(file_name, key_word):
    with open(file_name, 'r') as f:
        for line in f:
            if key_word in line:
                print(line)

search_diary('diary.txt', 'i')


def safe_raed_diary(file_name):
    try:
        with open(file_name, 'r') as f:
            f.read()
    except:
        print("the file is not exist")

safe_raed_diary('bla.txt')



"""
תרגיל 2
"""
def create_grades_file(file_name):
	students = [
 	("Dan", [85, 90, 78]),
 	("MOMO", [92, 88, 95]),
 	("Yoni", [70, 65, 80]),
 	("Avi", [100, 95, 98]),
	("Sara", [60, 72, 68])
	]
	with open(file_name, 'w',encoding="UTF-8") as f:
		for line in students:
			f.write(f"{line[0]}, {line[1][0]}, {line[1][1]}, {line[1][2]}\n")
	
create_grades_file("grades.txt")



def calculate_average(file_name):
	avrg = {}

	with open(file_name, 'r') as f:
		for stu in f:
			stu = stu.split(", ")
			count = 0
			sum_of = 0
			for i in range(1, len(stu)):
				sum_of += int(stu[i])
				count += 1
			avrg[stu[0]] = sum_of / count

	return avrg


results = calculate_average('grades.txt')
for name, avg in results.items():
	print(f'{name}: {avg:.1f}')
	

def save_results(avrgs, file_name):
	with open(file_name, 'w') as f:
		f.write("=== Student Results ===\n")
		
		i = 0
		sum_of_avrg = 0
		count_of_stu = 0
		max_avrg = 0
		min_avrg = 100
		sorted_dict = dict(sorted(avrgs.items(), key=lambda item: item[1], reverse=True))
		for name, avrg in sorted_dict.items():
			i += 1
			f.write(f"{i}. {name}: {avrg}\n")
			sum_of_avrg += avrg
			count_of_stu += 1
			max_avrg = max(max_avrg, avrg)
			min_avrg = min(min_avrg, avrg)
		f.write("\n=== Statistics ===\n")
		f.write(f'average of average: {sum_of_avrg//count_of_stu}\n')
		f.write(f'max average: {max_avrg}\n')
		f.write(f'min average: {min_avrg}')
			
save_results(results, 'result.txt')


