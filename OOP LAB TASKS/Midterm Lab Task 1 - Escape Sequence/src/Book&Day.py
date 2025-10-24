
bookTitle = input("Enter your book title: ")
author = input("Enter your author: ")
year = input("Enter your year: ")
genre = input("Enter your genre: ")
library = input("Enter your library: ")
returnDate = input("Enter your return date: ")

print(f"You have successfully entered reserved the book {bookTitle}\n"
      f"Year of publication: {year}\n"
      f"Genre: {genre}\n"
      f"Library: {library}\n"
      f"Return date: {returnDate}\n")
print()

day = int(input("Enter day: "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
