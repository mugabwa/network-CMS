from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, full_name, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email is required!'))
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, password=password, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, full_name, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must be staff'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser true'))
        return self.create_user(full_name, email, password, **extra_fields)