class User:
    name= None
    email= None
    def send_email(self):
        if self.email is not None:
                print("sending email:" + self.email)
        else:
             print("error")
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def __str__(self):
         return "User:" + self.email
per1 =User("israel","21185@virtual.utsc.edu.mx")
per1.send_email()

class Student(User):
     id=None
     def __init__(self,name=None,email=None, id= None, score= None ):
        super().__init__(name, email)
        self.id = id
        self.score = score

     def __str__(self):
          return "Student."+str(self.id)+"," + self.email 
     
     def __repr__(self):
          return f"Student(name='{self.name}',email='{self.email}',id='{self.id}')"

student1=Student("isra","21185@virtual.utsc.edu.mx")
student1.send_email()
student2=Student(email="isra.mont53@gmail.com")
student2.send_email()
print(student1.id,student2.id)

user1=User("isra","21185@virtual.utsc.edu.mx")
print(user1)
student1=Student(name="isra",email="21185@virtual.utsc.edu.mx")
print(student1)

def is_approved(self):
     return self.score >=8
def __repr__(self):
     return f"Student(name='{self.name}', email='{self.email}', id='{self.id}', score='{self.score}')"
     print ([student_score1])
