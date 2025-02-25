
l = []

def signIn():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    for user in l:
        if user['email'] == email:
            if user['password'] == password:
                print("Login successful.")
                return
            else:
                print("Incorrect password.")
                return
    print(f"{email} is not registered, please sign up first.")

def signUp():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    # Check if email already exists
    for user in l:
        if user['email'] == email:
            print("Email already registered. Please sign in.")
            return

    l.append({"email": email, "password": password})
    print("Signup successful.")

def main():
    while True:
        key = input("\nEnter 1 for signup...\nEnter 2 for signin...\nEnter 3 to exit...\n")
        
        if key == "3":
            break
        elif key == "1":
            signUp()
        elif key == "2":
            signIn()
        else:
            print("Please enter a valid option.")

if __name__ == "__main__":
    main()
