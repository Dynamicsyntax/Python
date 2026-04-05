#19. 🧵 String Reversal

string_to_check = input("Enter a string to reverse: ")
length_of_string = len(string_to_check)
reversed_string = ""

for i in range(length_of_string - 1, -1, -1):
    reversed_string += string_to_check[i]

print(f"🔄 Reversed String: {reversed_string}")
