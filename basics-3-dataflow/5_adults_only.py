
students = [
    ('Rama'  , 18),
    ('Alice' , 17),
    ('Bob'   , 21),
    ('Sunder', 17),
    ('Arjun' , 22),
    ('Alex'  , 17),
]

adults = filter(lambda student: student[1] >= 18 , students)
print ""
print  "ABOVE 18 Students are : ", ", ".join([student[0] for student in adults])
print ""
print "\n".join(map(lambda student: "{0[0]} is {0[1]} years old and is an adult!".format(student), adults))
