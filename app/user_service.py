class User:
    def __init__(self, email, name):
        self.email = email
        self.name = name


class UserService:
    def __init__(self):
        self.users = {}

    def create_user(self, user):
        if user.email in self.users:
            return False
        self.users[user.email] = user
        return True

    def get_user(self, email):
        return self.users.get(email)

    def update_user(self, user):
        if user.email not in self.users:
            return False
        self.users[user.email] = user
        return True

    def delete_user(self, email):
        if email not in self.users:
            return False
        del self.users[email]
        return True