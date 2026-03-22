rows = 5

for i in range(rows):
    
    # print leading single spaces
    for space in range(i):
        print(" ", end="")
    
    # print stars
    for star in range(rows - i):
        print("* ", end="")
    
    print()