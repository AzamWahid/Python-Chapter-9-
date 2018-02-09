class Student():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 18
        self.rollNo = 15
        self.GPA = 3.5

    def study(self):
        print(self.first_name + ' study very Well')
        print(self.first_name + ' age is ' + str(self.age))
        print(self.first_name + ' roll no. is ' + str(self.rollNo))

    def exam(self):
        print(self.first_name + ' give exam carefully')

    def assinment(self):
        print(self.first_name + ' Make assignments clearly')

    def extra_activity(self):
        print(self.first_name + ' participate in every activity')

    def checkingAssignment(self):
        print(self.first_name,self.last_name)


students = Student("Azam","A.Wahid")
students.study()
students.exam()
students.assinment()
students.extra_activity()
students.checkingAssignment()

class Teacher_assistant(Student):

    def __init__(self, first_name, last_name,teacheName):
        super().__init__(first_name,last_name)
        self.teacherName = teacheName
        #self.age = 18
        #self.rollNo = 15

    def checkingAssignment(self):
        print('This Student '+self.first_name+' Checks Assignment of '+self.teacherName + 'along with GPA : '+str(self.GPA))

a = Teacher_assistant('Azam','Wahid','Sir Ijaz')
a.checkingAssignment()