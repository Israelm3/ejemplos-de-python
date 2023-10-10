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

#list1 = list()
#for i in range(3):
#     list1.append(str(uuid.uuid4()))
#print(list1)

list1 = [
     '891200ac-446c-496d-b1a5-7cdb70744536', 
     '0a526e9a-82ea-4e3b-a7df-5ab99cd78175', 
     'f2df5d96-3d8f-4802-9279-ffabd732e79e',
]

dict1 = dict()
for i,uuid_str in enumerate (list1):
     dict1[uuid_str] = Student(
          name="student" + str (i),
          email="email" + str(i) + "@utsc.edu.mx",
          id=uuid_str

     )
print(dict1) 
print(dict1['f2df5d96-3d8f-4802-9279-ffabd732e79e'])
dict2={'891200ac-446c-496d-b1a5-7cdb70744536': Student(name='student0',email='email0@utsc.edu.mx',id='891200ac-446c-496d-b1a5-7cdb70744536'), '0a526e9a-82ea-4e3b-a7df-5ab99cd78175': Student(name='student1',email='email1@utsc.edu.mx',id='0a526e9a-82ea-4e3b-a7df-5ab99cd78175'), 'f2df5d96-3d8f-4802-9279-ffabd732e79e': Student(name='student2',email='email2@utsc.edu.mx',id='f2df5d96-3d8f-4802-9279-ffabd732e79e')}
