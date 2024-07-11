from django.db import models


# Create your models here.
class Diet(models.Model):
    user_id = models.IntegerField(null=True)
    record_date = models.DateTimeField(null=True)
    breakfast = models.TextField(null=True)
    breakfast_weight = models.FloatField(null=True)
    breakfast_heat = models.FloatField(null=True)
    lunch = models.TextField(null=True)
    lunch_weight = models.FloatField(null=True)
    lunch_heat = models.FloatField(null=True)
    dinner = models.TextField(null=True)
    dinner_weight = models.FloatField(null=True)
    dinner_heat = models.FloatField(null=True)
    note = models.TextField(null=True)
    sum = models.FloatField(null=True)

    class Meta:
        db_table = "diet"
