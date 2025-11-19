import random
import string

def generate_password(length=12):
    """Belirtilen uzunlukta rastgele bir şifre oluşturur."""
    characters = string.ascii_letters + string.digits + string.punctuation
    try:
        length = int(length)
        if length <= 0:
            return "Pozitif sayı kümesi kullan!"
        password = ''
        for i in range(length):
            password += random.choice(characters)
        return password
    except:
        return "Sayı giriniz!"

# Kullanım örneği
password_length = 12  # İstediğiniz herhangi bir şifre uzunluğunu seçebilirsiniz
print("Yeni şifreniz:", generate_password(password_length))
