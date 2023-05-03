from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None,first_name=None,last_name=None,is_active=True,is_staff=False,is_admin=False):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a valid username')
        if not password:
            raise ValueError('Users must have a valid password')

        user_obj = self.model(
            email=self.normalize_email(email)
        )

        user_obj.set_password(password)
        user_obj.username = username
        user_obj.first_name= first_name
        user_obj.last_name =last_name
        user_obj.isAdmin = is_admin
        user_obj.isActive = is_active
        user_obj.isStaff = is_staff

        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, username, password=None,first_name=None,last_name=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_active=True,
            is_staff=True,
            is_admin=True
        )

        return user

