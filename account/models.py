from django.db import models


# Create your models here.
class Account(models.Model):
    username = models.TextField(null=True)
    email = models.TextField(null=True)
    phone = models.TextField(null=True)
    password = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True)

    class Meta:
        db_table = "account"
