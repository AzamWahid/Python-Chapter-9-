from studentClass import Student

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