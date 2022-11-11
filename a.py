from django.core.management.utils import get_random_secret_key

class SigningKey:
    def __str__(self):
        return get_random_secret_key()

print(SigningKey())
print(SigningKey())
print(SigningKey())