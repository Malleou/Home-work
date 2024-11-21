grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
rating_stud = {}

sort_stud = sorted(students)
for rating in range(len(sort_stud)):
    rating_stud[sort_stud[rating]] = sum(grades[rating]) / len(grades[rating])
print(rating_stud)