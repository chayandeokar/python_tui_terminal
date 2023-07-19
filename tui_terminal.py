import os

os.system("tput setaf 1")
print("\t\t\t Welcome to Linux World")

os.system("tput setaf 7")
print("\t\t\t ------------")

while True:
    print("""
    press 1 : To See Date
    press 2 : To check Cal
    press 3 : To Setup Account
    press 4 : To create file
    """
    )

ch = input("Enter your Choice : ")
print(ch)

if int(ch) == 1:
  os.system("date")
elif int(ch) == 2:
  print("cal")
elif int(ch) == 3:
  print("user")
elif int(ch) == 4:
  print("file")
else:
  print("No Support")

input("press Enter to Cont....")
os.system("clear")
