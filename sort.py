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
students = ("Squid", "Sandy", "Patrick", "Spongebob", "Karbs")
sorted_students = sorted(students, reverse=True)

for i in sorted_students:
    print(i)
