from django.db import models

class User(models.Model):
    f_name = models.CharField(max_length=264, unique=True)
    l_name = models.CharField(max_length=256,null=True)
    email = models.EmailField(max_length=70, blank=True)

    def __st__(self):
        return self.f_name
