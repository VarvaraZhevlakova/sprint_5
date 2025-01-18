import random
import string


def generate_email(domain="example.com"):
    """Генерирует случайный email адрес."""
    random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    email = f"{random_name}@{domain}"
    return email

