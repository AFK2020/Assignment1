

users=["Ahmad","Zainab","Hina","Ali"]

user_name=input("Enter user name")

users.append(user_name)

users[0],users[-1]= users[-1],users[0]

print(users)