# Read from file and convert content to uppercase

# Open file in read mode
with open("input.txt", "r") as file:
    content = file.read()

# Convert to uppercase
upper_content = content.upper()

# Display result
print("Uppercase Content:\n")
print(upper_content)