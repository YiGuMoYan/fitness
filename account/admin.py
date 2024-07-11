from django.contrib import admin

from account.models import Account

# Register your models here.
admin.site.register(Account)
admin.site.site_title = "GymPro"
admin.site.site_header = "GymPro"
admin.site.index_title = "GymPro"
