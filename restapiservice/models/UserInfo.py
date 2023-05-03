from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .appusermanager import MyUserManager
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.
# By default AbstractBaseUser has details: id password lastlogin


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}

class UserInfo(AbstractBaseUser,PermissionsMixin):
    
    username = models.CharField(max_length=70,unique=True)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.CharField(verbose_name="email",max_length=60,unique=True)
    created = models.DateTimeField(auto_now_add=True,blank=True)
    isActive = models.BooleanField(default=True)
    isStaff=models.BooleanField(default=False)
    isAdmin= models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name="date joined",default=timezone.now)
    date_of_birth = models.DateField(verbose_name="date of birth",blank=True,default=timezone.now)
    date_modified = models.DateTimeField(db_column="date modified",auto_now=True)
    phone = models.CharField(max_length=15,blank=True)
    auth_provider = models.CharField(max_length=255, blank=False,null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD= 'email'

    REQUIRED_FIELDS = ['username', 'first_name','last_name']  #USERNAME_FIELD and password are required by default

    objects = MyUserManager()

    class Meta:
        db_table = 'UserAccount'

    def __str__(self):      # “magic method” that returns a string representation of any object
        return self.email

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
        
    def tokens(self):
        print("token started")
        refresh = RefreshToken.for_user(self)
        return {'refresh': str(refresh),'access': str(refresh.access_token)}

    @property
    def is_active(self):
        return self.isActive

    @property
    def is_admin(self):
        return self.isAdmin

    @property
    def is_staff(self):
        return self.isStaff

