from django.db import models


# Create your models here.
class Fit(models.Model):
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    image = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "fitness"
