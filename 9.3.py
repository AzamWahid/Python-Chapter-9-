class user():
    def __init__(self,first_name,last_name,username,email,location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print("\n" + self.first_name + " " +self.last_name)
        print("User Name: " + self.username)
        print("email: " + self.email)
        print("location: "+self.location)

    def greet_user(self):
        print("\nWelcome " + self.username)


azhi = user('Azam' , 'A.Wahid','muhammadAzam',"azamwahid@outlook.com","Karachi")
azhi.describe_user()
azhi.greet_user()

azhi = user('Abdul Qadir' , 'A.Wahid','abdulqadir',"Qadir.memon@professional.biz.pk","Karachi")
azhi.describe_user()
azhi.greet_user()
