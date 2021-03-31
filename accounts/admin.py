import profile

from django.contrib import admin

from accounts.models import Profile, Payment

admin.site.register(Profile)
admin.site.register(Payment)
