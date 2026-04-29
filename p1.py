def register():
    f = open("file.txt", "a")
    username = input("Enter username: ")
    password = input("Enter password: ")
    f.write(username + "," + password + "\n")
    f.close()
    print("Registration Successful")


def login():
    found = False

    f = open("file.txt", "r")
    username = input("Enter username: ")
    password = input("Enter password: ")

    for line in f:
        u, p = line.strip().split(",")
        if u == username and p == password:
            print("Login successful")
            found = True
            break

    f.close()

    if not found:
        print("Login failed \n You have to register first")


print("1. Signup")
print("2. Signin")
print("3. Exit")

n = int(input("Enter choice: "))

if n == 1:
    register()
elif n == 2:
    login()
elif n == 3:
    print("Thank you for your visit")
else:
    print("Enter a valid choice")
