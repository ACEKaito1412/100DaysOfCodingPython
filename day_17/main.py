class User:
    def __init__(self, user_id, f_name, l_name):
        self.id = user_id
        self.f_name = f_name
        self.l_name = l_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.followers += 1
        user.following += 1

user_1 = User("001", "Ace", "Kaito")
user_2 = User("002", "Alpha", "Rem")

user_1.follow(user_2)
print(user_1.followers)
print(user_2.following)
