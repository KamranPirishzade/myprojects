class FollowCheck:
    def __init__(self,username,id):
        self.username=username
        self.id=id
        self.followers=0
        self.following=0

    def follow(self,user):
        user.followers+=1
        self.following+=1

user1=FollowCheck("Kamran","15")

user2=FollowCheck("Hasan","12")

user1.follow(user2)
print(user1.following)
print(user1.followers)
print(user2.followers)
print(user2.following)
