def railfence_cipher(text, num_rails):
    if num_rails <= 1:
        return text  # No encryption needed if rails = 1

    rail = ['' for _ in range(num_rails)]  # Create rails as separate strings
    direction = 1  # Direction: 1 for down, -1 for up
    row = 0

    # Fill the rail fence in a zigzag manner
    for char in text:
        rail[row] += char  # Append character to the correct row
        if row == 0:
            direction = 1  # Move down
        elif row == num_rails - 1:
            direction = -1  # Move up
        row += direction

    return ''.join(rail)  # Concatenate rows to form ciphertext

# Example usage:
plaintext = input("Enter your message: ")
rails = int(input("Enter the no. of rails: "))
ciphertext = railfence_cipher(plaintext, rails)
print(f"Ciphertext: {ciphertext}")
