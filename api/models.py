from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phone_field import PhoneField
class Usermanager(BaseUserManager):
    def create_user(self, email, phone,  password=None,):
        if email is None:
            raise TypeError("Users should have a email")
        user=self.model(phone=phone, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError('Password should not a none')
        user=self.create_user( email, password)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    phone=PhoneField(blank=False, help_text='Contact phone number')
    email=models.EmailField(max_length=225, unique=True, db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active =models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    creater_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username']

    objects = Usermanager()

    def __str__(self):
        return self.email

