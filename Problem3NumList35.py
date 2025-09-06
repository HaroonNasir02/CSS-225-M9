# Muhammad Haroon Nasir
# 05/09/25

# Problem 3: A while loop that asks user for a value, appends that value to a list and sums up the list. While loop runs till sum is above 100

# Initialize an empty list to store numbers
numbers = []

# Initialize a variable to keep track of the sum
total = 0

# Continue asking the user until the sum is greater than 100
while total <= 100:
    num = float(input("Enter a number: "))
    numbers.append(num)
    total += num
    print(f"Current list: {numbers}, Current sum: {total}")

print("\nFinal list of numbers:", numbers)
print("Total sum:", total)
print("Sum exceeded 100! Loop ended.")