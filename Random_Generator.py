import random

def generate_random_block(height, width):
    block = ''
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-'
    
    for _ in range(height):
        line = ''.join(random.choice(characters) for _ in range(width))
        block += line + '\n'
    
    return block

# Prompt user for height and width
height = int(input("Enter the desired height: "))
width = int(input("Enter the desired width: "))

# Generate random block
random_block = generate_random_block(height, width)

# Save the random block to a file
with open("Test.txt", "w") as file:
    file.write(random_block)

print("Random block saved to Test.txt.")