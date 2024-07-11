from django.db import models


# Create your models here.
class GymLocation(models.Model):
    province = models.TextField(null=True)
    city = models.TextField(null=True)
    address = models.TextField(null=True)
    name = models.TextField(null=True)

    class Meta:
        db_table = "gym"
