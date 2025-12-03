def text_to_binary(text):
    """Convert text to binary."""
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    """Convert binary to text."""
    return ''.join(chr(int(b, 2)) for b in binary.split())

if __name__ == "__main__":
    print("What would you like to do?")
    print("1. Convert text to binary")
    print("2. Convert binary to text")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        text = input("Enter the text to convert to binary: ")
        binary_result = text_to_binary(text)
        print(f"Binary representation: {binary_result}")
    elif choice == "2":
        binary = input("Enter the binary to convert to text (separate bytes with spaces): ")
        text_result = binary_to_text(binary)
        print(f"Text representation: {text_result}")
    else:
        print("Invalid choice. Please run the program again and select 1 or 2.")