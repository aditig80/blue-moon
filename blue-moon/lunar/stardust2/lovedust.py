from cryptography.fernet import Fernet

def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()

if __name__ == "__main__":
    try:
        # Fixed secret key
        secret_key = b'JqlLeXFCMqg9k5ZsDr7CxgeZMKTqUZnlWcqv1l4JwLY='
        
        # Encrypted message
        encrypted_message = b'gAAAAABn6Sp7WvseI5iuIzWbOURA-Q9sCw30rLroTBJWGLIjYr_xu_bZp6YbK-j-QKnaacXX87TGy8NZl79pHhXU14r5JsSQiA=='
        
        # Decrypt and print
        decrypted_message = decrypt_message(encrypted_message, secret_key)
        print(f"The decrypted message is: {decrypted_message}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
