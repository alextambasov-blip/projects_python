groupmates = [
    {"name": "Александр", "surname": "Тамбасов", "exams": ["Информатика","Математика"], "marks":[4,5]},
    {"name": "Фёдор", "surname":"Цуканов", "exams":["История","Физика"], "marks":[3,4]},
    {"name": "Артём", "surname":"Локтев", "exams":["Философия","ИС"], "marks":[5,5]},
]

def avg(marks):
    return sum(marks)/len(marks) if marks else 0

def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(15), "Экзамены".ljust(30), "Оценки".ljust(20), "Средний")
    for s in students:
        print(s["name"].ljust(15), s["surname"].ljust(15), str(s["exams"]).ljust(30), str(s["marks"]).ljust(20), f"{avg(s['marks']):.2f}")

def filter_by_min_avg(students, min_avg):
    return [s for s in students if avg(s["marks"]) > min_avg]

if __name__ == "__main__":
    print_students(groupmates)
    try:
        m = float(input("Введите порог среднего (например 4.0): "))
    except:
        m = 4.0
    print("\nСтуденты с средним > ", m)
    print_students(filter_by_min_avg(groupmates, m))
