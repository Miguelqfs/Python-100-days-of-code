class UserClass: #Pascal Case
    # PascalCase
    # camelCase (not common in python)
    # snake_case
    def __init__(self, user_name, user_id): # Special function to initialize attributes of an object
                                    # 'self' refers to the created object
        print("New user is being created...")
        self.name = user_name # .name is the name of the attribute witch is going to be initialized by __init__
        self.id = user_id
        self.followers = 0 # It doesn't have to be a parameter
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = UserClass("Miguel", "001")
user_2 = UserClass("Marina", "002")

print(f"{user_1.name}: {user_1.id}")
print(f"{user_2.name}: {user_2.id}")

user_1.follow(user_2) # User 1 (Miguel) starts to follow user 2 (Marina).
print(f"{user_1.name} is following {user_1.following} people")
print(f"{user_2.name} has {user_2.followers} followers")