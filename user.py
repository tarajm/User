
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        #default attributes
        self.is_rewards_member = False
        self.gold_card_points = 0
    

    # display_info(self) - Have this method print all of the users' details on separate lines.
    #is there a way to do this using the /n where items are printed on a separate line?

    ##update assignment showing each instance being chained
    def display_info(self):
        print(f'First Name:  {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Email Address: {self.email}')
        print(f'Age: {self.age}')
        print(f'Rewards Member? {self.is_rewards_member}')
        print(f'Current Gold Card Points: {self.gold_card_points}')
        print('\n')  #creates a space between outputs


# Have this method change the user's member status to True and set their gold card points to 200.
# Add logic in the enroll method to check if they are a member already, and if they are, 
# print "User already a member." and return False, otherwise return True.
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member")
            return False
        self.is_rewards_member = True 
        self.gold_card_points = 200
        print('\n')
        


#Have this method decrease the user's points by the amount specified.
# Add logic in the spend points method to be sure they have enough points 
# to spend that amount and handle appropriately.

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Not enough points!")
            return
        self.gold_card_points -= amount
        print('\n')



#############

tara = User("Tara", "Massan", "tarajmassan@gmail.com", 75)
# tara.display_info()
# tara.enroll()
# tara.display_info()
# tara.spend_points(500)
# tara.display_info()

tara.display_info().


################
# second_user = User("Jake", "Blue", "someemail@gmail.com", 99)
# second_user.display_info()
# second_user.spend_points(80)
# second_user.display_info()

