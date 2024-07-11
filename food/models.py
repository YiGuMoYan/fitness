from django.db import models


# Create your models here.
class Food(models.Model):
    name = models.TextField(null=True)
    heat = models.FloatField(null=True)

    class Meta:
        db_table = "food"
