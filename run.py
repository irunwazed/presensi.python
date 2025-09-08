from cryptography.fernet import Fernet
import runpy

key = b"5yOnRRrVpPLC6eyPc7QD17mPTan913vHzMFwzRAQwUE="

cipher = Fernet(key)

# Baca file terenkripsi
with open("app.py", "rb") as f:
    encrypted_code = f.read()

# Dekripsi kode Python
decrypted_code = cipher.decrypt(encrypted_code)

# Jalankan kode Python yang sudah didekripsi secara runtime
exec(decrypted_code, globals())
