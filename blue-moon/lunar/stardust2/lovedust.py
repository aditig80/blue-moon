from cryptography.fernet import Fernet
import requests

def get_secret_key():
    response = requests.get("https://httpbin.org/uuid")
    if response.status_code == 200:
        uuid = response.json()["uuid"]
        key_base = uuid.replace("-", "")[:32].ljust(32, "0")
        key = Fernet.generate_key()
        return key
    else:
        raise Exception("Failed to fetch the secret key! Please check your internet connection.")

def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()

if __name__ == "__main__":
    try:
        secret_key = get_secret_key()
        encrypted_message = b'gAAAAABlxAbc36lTjUBp7RdLdsowYQMbvrMtiRRdWpj9u4QeK7JzR_kvtEAXZ6vQAkJe4Ej3E5uXT2N2Q9NLKDh_GuH9aF-DVA=='
        decrypted_message = decrypt_message(encrypted_message, secret_key)
        print(f"The decrypted part of the flag is: {decrypted_message}")
    except Exception as e:
        print(f"An error occurred: {e}")
