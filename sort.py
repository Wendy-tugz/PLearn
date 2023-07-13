#sort() method = used with lists
#sort() function = used with iterables


#sort method
# students = ["Squid", "Sandy", "Patrick", "Spongebob", "Karbs"]
#
# students.sort()
#
# for i in students:
#     print(i)


#sort function
# students = ("Squid", "Sandy", "Patrick", "Spongebob", "Karbs")
# sorted_students = sorted(students, reverse=True)
#
# for i in sorted_students:
#     print(i)


#tuple
students = [("Squid", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Karbs", "C", 78)]

# grade = lambda grades: grades[1]
# students.sort(key=grade, reverse=True)

age = lambda ages: ages[2]
students.sort(key=age)

for i in students:
    print(i)
