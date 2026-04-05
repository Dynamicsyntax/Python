#41. 📊 Number Comparison Tool

import statistics

numbers = []
count = int(input("Enter how many numbers you want to enter: "))

for i in range(count):
    number = float(input(f"Enter number {i+1}: "))
    numbers.append(number)

print(f"✅ You entered: {numbers}")

# Compute min, max, and median
minimum = min(numbers)
maximum = max(numbers)
median = statistics.median(numbers)

print(f"🔹 Minimum value = {minimum}")
print(f"🔹 Maximum value = {maximum}")
print(f"🔹 Median value = {median}")
