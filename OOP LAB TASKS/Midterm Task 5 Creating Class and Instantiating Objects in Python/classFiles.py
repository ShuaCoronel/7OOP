
class Person:
    def __init__(self, first_name, last_name, followers,friends):

        self.first_name = first_name
        self.last_name = last_name
        self.followers = followers
        self.friends = friends


    def introduce_self(self):
        print()
        print(f"Hi {self.first_name} {self.last_name}!")
        print(f"Profile Name: {self.first_name} {self.last_name}\n{self.followers} followers")
        print("Friends:",end = " ")
        for friend in self.friends:
            print(f"{friend}", end= ',')

    def number_of_human(self, people):
        print(f"\n{len(people)} member to your social media page!")


#testfunctions
def testperson():
    testPersonList = []
    while True:

        choice = input("Testing press y for yes/n to stop:").lower()
        if choice == "n":
            break
        firstName = input("Enter your first name: ")
        lastName = input("Enter your last name: ")
        followers = input("Enter your followers: ")
        testFriendList = []

        while True:
            friendinput = input("Enter your friends: 0 to stop: ")
            if friendinput == "0":
                break
            testFriendList.append(friendinput)

        person = Person(firstName, lastName, followers, testFriendList )
        testPersonList.append(person)
        print()

    for human in testPersonList:
        human.introduce_self()


    person.number_of_human(testPersonList)


if __name__ == "__main__":

    testperson()
