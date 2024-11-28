def decrypt_message(message: str) -> str:
    """
    Decrypts a message by removing all numeric characters.

    Args:
        message (str): The encrypted message containing alphanumeric characters.

    Returns:
        str: The decrypted message with numeric characters removed.
    """
    decrypt_message = ""
    for char in message:
        if not char.isnumeric():
            decrypt_message += char
    return decrypt_message

def main() -> None:
    strange_message = "432H3525el523l52o5 523C532F52"
    decrypted_message =decrypt_message(strange_message)
    print(decrypted_message)

if __name__ == "__main__":
    main()