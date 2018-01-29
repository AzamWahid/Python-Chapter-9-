class user():
    def __init__(self,first_name,last_name,username,email,location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " +self.last_name)
        print("User Name: " + self.username)
        print("email: " + self.email)
        print("location: "+self.location)

    def greet_user(self):
        print("\nWelcome " + self.username)

    def increment_login_attempts(self):
        self.login_attempts+=1
    def rest_login(self):
        self.login_attempts = 0


azhi = user('Azam' , 'A.Wahid','muhammadAzam',"azamwahid@outlook.com","Karachi")
azhi.describe_user()
azhi.greet_user()
print('--------------------Increment login attempt------------------------------')
azhi.increment_login_attempts()
print('Login Attempts:' + str(azhi.login_attempts))
print('--------------------Reset login attempt------------------------------')
azhi.rest_login()
print('Reset Login: '+str(azhi.login_attempts))


azhi = user('Abdul Qadir' , 'A.Wahid','abdulqadir',"Qadir.memon@professional.biz.pk","Karachi")
azhi.describe_user()
azhi.greet_user()