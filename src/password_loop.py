attempts_left = 3
correct_password = "secret"

while attempts_left > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted ✅")
        break
    else:
        attempts_left -= 1
        print(f"Wrong password ❌. Attempts left: {attempts_left}")

if attempts_left == 0:
    print("Locked out 🔒")