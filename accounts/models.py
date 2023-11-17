from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class MyAccountManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, password=None):
        user = self.model(
                username = username, first_name = first_name,
                last_name = last_name
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, password):
        user = self.create_user(
                username = username, first_name = first_name,
                last_name = last_name,
                password = password
            )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(max_length = 60)
    username = models.CharField(max_length = 30, unique = True)
    date_joined = models.DateField(auto_now_add = True)
    last_login = models.DateTimeField(auto_now = True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = MyAccountManager()

    def __str__(self):
            return self.first_name + " " + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True
