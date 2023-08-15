from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from config.settings import MEDIA_URL, STATIC_URL


class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    def get_image(self):
        if self.image:
            return f'{MEDIA_URL}{self.image}'
        return f'{STATIC_URL}img/empty.png'