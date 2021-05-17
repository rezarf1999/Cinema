from django.contrib import admin

from accounts.models import Profile, Payment


class ProfileAdmin(admin.ModelAdmin):
    list_filter = ['user', 'city']
    search_fields = ['user']
    list_display = ['user', 'gender', 'city', 'phone']


admin.site.register(Profile, ProfileAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_filter = ['transaction_time']
    search_fields = ['profile', 'transaction_code']
    list_display = ['profile', 'amount', 'transaction_time', 'transaction_code']


admin.site.register(Payment, PaymentAdmin)
