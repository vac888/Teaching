from django.db import models
from django.contrib.auth.models import User
import uuid

class APIKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return uuid.uuid4().hex

    def __str__(self):
        return self.key
    

class APIKeyUsage(models.Model):
    api_key = models.ForeignKey(APIKey, on_delete=models.CASCADE)  # Связь с APIKey
    used_at = models.DateTimeField(auto_now_add=True)  # Время использования
    request_ip = models.GenericIPAddressField(blank=True, null=True)  # IP-адрес запроса
    request_method = models.CharField(max_length=10, blank=True, null=True)  # Метод запроса (GET, POST и т.д.)

    def __str__(self):
        return f"Usage of {self.api_key.key} at {self.used_at}"
    
