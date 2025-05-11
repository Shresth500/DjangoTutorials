from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from profiles_project import settings


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Managers for User Profile"""
    """Can Manipulate objects and return that object"""

    def create_user(self, name,email, password=None):
        if not email:
            raise ValueError('User Must have an email address')
        
        if not name:
            raise ValueError("User must enetr a user name")
        
        if not password:
            raise ValueError('User must enter a password')
        
        email = self.normalize_email(email=email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using = self._db)

        return user
    
    def create_superuser(self,name,email,password=None):
        """Creating super user"""

        user = self.create_user(name=name,email=email,password=password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)
        return user




class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # we need to specify the user field to the unique field of our preference
    # This is because we are overriding the default USERNAME Field which is normally called user name
    # Because we need to use email and password instead of username and password
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] # Additional Required Fields apart from email and password

    def get_full_user_name(self):
        """Retrieve User Name"""
        return self.name
    
    def get_short_name(self):
        """Retrieve Short Name of User"""
        return self.name.lower()
    
    # convert a user profile object to a string in python
    def __str__(self):
        return self.email
    

class ProfileFeedItem(models.Model):
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text