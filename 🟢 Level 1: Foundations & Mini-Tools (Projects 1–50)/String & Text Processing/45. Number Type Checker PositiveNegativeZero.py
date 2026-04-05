#45. 🔢 Number Type Checker

number = input("Enter a number to check its type: ")

if number.isdigit():
    number = int(number)
    if number > 0:
        print("✅ Number is Positive")
    elif number < 0:
        print("✅ Number is Negative")
    else:
        print("✅ Number is Zero")
else:
    print("❌ Please enter valid numbers")
