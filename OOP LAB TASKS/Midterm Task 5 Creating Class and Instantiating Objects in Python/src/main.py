
from classFiles import Person

people = []
while True:

    choice = input("Insert a record? (y/n): ").lower()
    if choice == "n":
        print()
        break

    firstName = input("Insert a first name: ")
    lastName = input("Insert a last name: ")
    followers = int(input("Insert a followers: "))

    tempList = []
    while(True):

        friendInput = input("Insert a friend/s(press 0 to exit): ")
        if friendInput == "0":
            print()
            break
        else:
            tempList.append(friendInput)

    human = Person(firstName, lastName, followers, tempList)
    people.append(human)

print("\nHere are the records:")
for person in people:
    person.introduce_self()
    print()

human.number_of_human(people)
