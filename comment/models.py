from django.db import models


# Create your models here.
class Comment(models.Model):
    user_id = models.IntegerField(null=True)
    share_id = models.IntegerField(null=True)
    content = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comment"
