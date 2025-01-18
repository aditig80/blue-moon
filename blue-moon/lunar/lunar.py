import base64

def generate_key(seed):
    return ''.join([chr(ord(c) + 1) for c in seed])

def decrypt_message(encoded, key):
    decoded = base64.b64decode(encoded).decode()
    decrypted = ''.join([chr(ord(c) ^ ord(k)) for c, k in zip(decoded, key)])
    return decrypted
if __name__ == "__main__":
    encoded_message = "U2FsdGVkX19uZYA1Mg=="
    key = generate_key("secretkey")

    decrypted_message = decrypt_message(encoded_message, key)

    if decrypted_message == "it's fake":
        print(decrypted_message)
    else:
        print("Error: Decryption failed.")
