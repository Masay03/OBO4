class UserManager():
    def __init__(self, user):
        self.user = user

    def change_user_name(self, user_name):
        self.user.name = user_name

    def seva_user(self):
        file = open("users.txt", "a")
        file.write(self.user.name + "\n")
        file.close()