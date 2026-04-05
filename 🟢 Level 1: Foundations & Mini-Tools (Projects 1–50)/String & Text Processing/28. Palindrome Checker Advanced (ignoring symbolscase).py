#28. 🔄 Palindrome Checker

main_word = input("Enter a word to check if it is a palindrome: ").strip()
reversed_word = main_word[::-1]

if main_word == reversed_word:
    print("✅ The word is a palindrome")
else:
    print("❌ The word is not a palindrome")
