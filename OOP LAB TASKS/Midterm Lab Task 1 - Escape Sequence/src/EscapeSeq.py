
name = input("Enter your name: ")
email = input("Enter your email: ")
university = input("Enter your university: ")

print("Name:\t", name)
print("Email:\t", email)
print("University:\t", university)
print()

sender = input("Sender: ")
version = int(input("Version: "))
discount = int(input("Discount: "))
status = input("Status: ")
code = int(input("Code: "))
location = input("Location: ")
age = int(input("Age: "))
company = input("Company: ")

print("Dear Dianne, I hope this email finds you well.\n"
      "I want to reach out and say hello \n"
      "I hope you are doing well and enjoying your day.... \n"
      "It's been a while since we last spoke,and I wanted to catch up with you\n"
      "lets plan to catch up soon and have a great time together!\n"
      "\n")
print(f"Sender: %s" %sender)
print(f"Version: %d" %version)
print(f"Discount: %d" %discount)
print(f"Status: %s" %status)
print(f"Code: %d" %code)
print(f"Location: %s" %location)
print(f"Age: %d" %age)
print(f"Company: %s" %company)
