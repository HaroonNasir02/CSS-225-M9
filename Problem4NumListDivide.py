# Muhammad Haroon Nasir
# 05/09/25

# Problem 4: A while loop with a counter, that runs till counter is 50. Appends all counter values that are divisible by 10 to a list

# Initialize an empty list to store values divisible by 10
tens = []

# Initialize counter
counter = 0

# Loop until counter reaches 50
while counter <= 50:
    if counter % 10 == 0:  # Check if divisible by 10
        tens.append(counter)
    counter += 1  # Increment counter

# Print the resulting list
print(tens)
