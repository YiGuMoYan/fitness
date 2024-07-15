from django.db import models


# Create your models here.
class TrainingLog(models.Model):
    user_id = models.IntegerField(null=True)
    date = models.DateField(null=True)
    duration = models.TextField(null=True)
    content = models.TextField(null=True)
    sets = models.TextField(null=True)
    reps = models.TextField(null=True)
    weight = models.TextField(null=True)

    class Meta:
        db_table = "training_log"
