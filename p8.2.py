with open("input.txt", "r") as file:
    content = file.read()

upper_content = content.upper()

# Write to output file
with open("output.txt", "w") as file:
    file.write(upper_content)

print("Uppercase content saved to output.txt")