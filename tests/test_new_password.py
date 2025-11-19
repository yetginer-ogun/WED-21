import string
from password.new_password import generate_password

def test_password_characters():
    """Şifre oluşturulurken yalnızca geçerli karakterlerin kullanıldığını test eder"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Daha güvenli bir doğrulama için uzun bir şifre oluşturuluyor
    for char in password:
        assert char in valid_characters

"""
Aşağıda önerilenlerden birini kullanarak başka bir test yazın. Alternatif olarak, kendi testinizi de oluşturabilirsiniz!
Daha fazla test yazabilirseniz harika olur!

1. Şifrenin uzunluğunun belirtilen uzunlukla eşleşip eşleşmediğini test edin  
2. Arka arkaya oluşturulan iki şifrenin farklı olup olmadığını test edin 
"""

def test_password_lenght():
    lenght = 100
    password = generate_password(lenght)
    assert len(password) == lenght

def test_password_default():
    password = generate_password()
    assert len(password) == 12

def test_password_difference():
    password = generate_password()
    password2 = generate_password()
    assert password != password2 

def test_password_lenght2():
    lenght = -5
    password = generate_password(lenght)
    assert password == "Pozitif sayı kümesi kullan!"