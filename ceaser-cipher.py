# Define the alphabet
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']

# Get user input
direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n ").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Define the Caesar cipher function
def caesar(original_text, shift_amount, encode_or_decode):
    cypher_text = ""
    
    if encode_or_decode == "decode":
        shift_amount *= -1  # Reverse shift for decryption

    for letter in original_text:
        if letter in alphabets:
            shifted_position = (alphabets.index(letter) + shift_amount) % len(alphabets)
            cypher_text += alphabets[shifted_position]
        else:
            cypher_text += letter  # Keep spaces and special characters unchanged
    
    print(f"The {encode_or_decode}d message is: {cypher_text}")

# Run the function
caesar(text, shift, direction)
