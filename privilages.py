class Privilages():
    def __init__(self):
        self.privileges = ['can add post',
                           'can delete post',
                           'can ban user']

    def show_privileges(self):
        print("Admin privilages")
        for privilage in self.privileges:
            print("- "+privilage)

    def get_privileges(self):
        current_privilege = []
        for privilage in self.privileges:
            current_privilege.append(privilage)
        return current_privilege


class User():

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.login_attempts = 0

    def greet_user(self):
        print("Hi "+self.first.title()+" " +
              self.last.title()+" welcome to the party!")

    def count_login_attempts(self):
        self.login_attempts += 1
        login_counts = self.login_attempts
        print("Login attempts "+str(login_counts))

    def reset_login_attempts_count(self):
        self.login_attempts = 0
        print("Login attempts reset to "+str(self.login_attempts))


class Admin(User):
    def __init__(self, first, last):
        super().__init__(first, last)
        self.privileges = Privilages()


user1 = Admin('ebo', 'riley')
user1.privileges.show_privileges()
