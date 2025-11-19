import random
import string

def generate_password(length=12):
    """Belirtilen uzunlukta rastgele bir şifre oluşturur."""
    characters = string.ascii_letters + string.digits + string.punctuation
    try:
        length = int(length)
        if length <= 0:
            return("şifre oluşturmayı bilmiyorsun gelmişsin burda siteye giriş yapmaya çalışıyorsun hadi yürü başka kapıya")
        password = ''
    
        for i in range(length):
            password += random.choice(characters)
        return password
    except Exception as e:
        print(e)
        return"sayı gir"

# Kullanım örneği
password_length = 12  # İstediğiniz herhangi bir şifre uzunluğunu seçebilirsiniz
print("Yeni şifreniz:", generate_password(password_length))
