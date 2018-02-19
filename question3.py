'''Create a Student class and initialize it with name and roll number. Make methods to :
a. Display - It should display all informations of the student.
b. setAge - It should assign age to student
c. setMarks - It should assign marks to the student.'''

class Student:
 age =0
 marks =0

 def __init__(self,name,roll):
  self.name = name
  self.roll = roll

 def setAge(self,age):
  self.age = age

 def setMarks(self,marks):
  self.marks = marks

 def Display(self):
  return "name:{} - roll:{} - age:{} - marks{}.".format(self.name, self.roll, self.age, self.marks)

s1=Student("aakhansya",85)
Student.setAge(s1,50)
print(s1.name,s1.roll)
print(s1.age)

Student.setMarks(s1,200)
print(s1.marks)

print(Student.Display(s1))
