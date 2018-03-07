from django.db import models
from django.contrib import auth
# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):
    # representacion en cadena del elemento, tipo tuiter
    def __str__(self):
        return "@{}".format(self.username)
