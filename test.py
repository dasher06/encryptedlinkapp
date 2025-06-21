import base64
from cryptography.fernet import Fernet

# Your 10-digit key (must match what you’ll enter on the form)
key = "1234567890"

# Pad the key to 32 bytes, just like your Flask app does
padded_key = key.ljust(32, '0').encode()

# Convert to Fernet-compatible key (URL-safe base64-encoded)
fernet_key = base64.urlsafe_b64encode(padded_key)

# Create a Fernet cipher
cipher = Fernet(fernet_key)

# This is the link you want to encrypt (you can use any link here)
link_to_encrypt = "https://drive.google.com/file/d/your-file-id/view"

# Encrypt the link
encrypted_link = cipher.encrypt(link_to_encrypt.encode()).decode()

# Print the result
print("🔐 Encrypted string to use in your test:")
print(encrypted_link)
print("\nUse this as the ?encrypted= parameter in your deployed URL")
