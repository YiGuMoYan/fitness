from django.db import models
from django.forms import forms


# Create your models here.
class Share(models.Model):
    user_id = models.IntegerField(null=True)
    title = models.TextField(null=True)
    content = models.TextField(null=True)
    image = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "share"


class UploadFile(forms.Form):
    file = models.ImageField(upload_to="")
