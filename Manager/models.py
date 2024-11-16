from django.db import models
from django.contrib.auth.models import AbstractUser
import random, string, json

class LoginDetails(AbstractUser):
    USER_TYPE_CHOICES = [
        ('ADMIN', 'admin'),
        ('TRAINER', 'trainer'),
        ('USER', 'user'),
        ('SHOPKEEPER', 'shopkeeper'),
        ('NUTRI_SPECIALIST', 'nutri_specialist'),
    ]
    
    user_type = models.CharField(max_length=22, choices=USER_TYPE_CHOICES, blank=True, null=True)
    status = models.CharField(default='active', max_length=100)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField('auth.Group', related_name='userprofile_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='userprofile_permissions', blank=True)

    def __str__(self):
        return self.username  # Display username for clarity


class Token(models.Model):
    key = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(LoginDetails, related_name="auth_tokens", on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    session_dict = models.TextField(default="{}")

    def __init__(self, *args, **kwargs):
        self.dict_ready = False
        self.data_dict = None
        super().__init__(*args, **kwargs)

    def generate_key(self):
        return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(40))

    def save(self, *args, **kwargs):
        if not self.key:
            new_key = self.generate_key()
            while Token.objects.filter(key=new_key).exists():
                new_key = self.generate_key()
            self.key = new_key
        super().save(*args, **kwargs)

    def read_session(self):
        self.data_dict = json.loads(self.session_dict) if self.session_dict != "null" else {}
        self.dict_ready = True

    def update_session(self, tdict, save=True, clear=False):
        if not clear and not self.dict_ready:
            self.read_session()
        if clear:
            self.data_dict = tdict
            self.dict_ready = True
        else:
            self.data_dict.update(tdict)
        if save:
            self.write_back()

    def set(self, key, value, save=True):
        if not self.dict_ready:
            self.read_session()
        self.data_dict[key] = value
        if save:
            self.write_back()

    def write_back(self):
        self.session_dict = json.dumps(self.data_dict)
        self.save()

    def get(self, key, default=None):
        if not self.dict_ready:
            self.read_session()
        return self.data_dict.get(key, default)

    def __str__(self):
        return str(self.user) if self.user else str(self.id)
