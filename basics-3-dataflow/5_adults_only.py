
students = [
    ('Rama'  , 18),
    ('Alice' , 17),
    ('Bob'   , 21),
    ('Sunder', 17),
    ('Arjun' , 22),
    ('Alex'  , 17),
]

adults = filter(lambda student: student[1] >= 18 , students)
print  "ABOVE 18 Students are : ", ", ".join([student[0] for student in adults]) 
