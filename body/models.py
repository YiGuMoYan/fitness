from django.db import models


# Create your models here.
class Body(models.Model):
    user_id = models.IntegerField(null=True)
    record_date = models.DateTimeField(null=True)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)

    class Meta:
        db_table = "body"
