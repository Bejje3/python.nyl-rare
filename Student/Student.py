class Student:
    def __init__(self, fname : str, lname : str, age : int, gender : str):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender 


    def __str__(self):
        return f"{self.fname} {self.age}"


class Teacher:
    def __init__(self, fname : str, lname : str, age : int, gender : str): 
        self.fname = fname 
        self.lname = lname 
        self.age = age  
        self.gender = gender 

class Group: 
    def __init__(self, subject :str, teacher : Teacher, students : list): 
        self.subject = subject 
        self.teacher = teacher 
        self.students = students




benjamin = Student("Benjamin", "Veizades", 17, "Man") 
manal = Teacher("Manal", "Idriss", 47, "man") 
programering = Group("Programering", manal, [benjamin])   


print(benjamin)
        
                                                