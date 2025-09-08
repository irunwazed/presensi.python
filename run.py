from cryptography.fernet import Fernet
import runpy

# Masukkan key hasil generate tadi di sini (harus sama dengan yang dipakai untuk encrypt)
key = b"leic57x2IYCd_VCgVd-0lMesjYuOkt0aRpy-Ez1dmhg="

cipher = Fernet(key)

# Baca file terenkripsi
with open("app.py", "rb") as f:
    encrypted_code = f.read()

# Dekripsi kode Python
decrypted_code = cipher.decrypt(encrypted_code)

# Jalankan kode Python yang sudah didekripsi secara runtime
exec(decrypted_code, globals())
