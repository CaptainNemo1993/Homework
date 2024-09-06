grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Student1={}
Johnny1=int(sum(grades[0]))/int(len(grades[0]))
Bilbo1=int(sum(grades[1]))/int(len(grades[1]))
Steve1=int(sum(grades[2]))/int(len(grades[2]))
Khendrik1=int(sum(grades[3]))/int(len(grades[3]))
Aaron1=int(sum(grades[4]))/int(len(grades[4]))
Student1={}
students2=list(students)
Student1.update({students2[0]: Johnny1,
                 students2[1]: Bilbo1,
                 students2[2]:Steve1,
                 students2[3]:Khendrik1,
                 students2[4]:Aaron1})
print(Student1)



