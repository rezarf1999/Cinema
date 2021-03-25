from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='حساب')
    avatar = models.ImageField('آواتار', upload_to='accounts_avatar/', null=True, blank=True)
    phone = models.IntegerField('تلفن همراه', null=False, max_length=20)

    woman = 1
    man = 2
    gender_choice = ((woman, 'زن'), (man, 'مرد'))
    gender = models.IntegerField('جنسیت', choices=gender_choice, blank=True, null=True)

    birthday = models.DateTimeField('تاریخ تولد', null=True, blank=True)
    credit_money = models.DecimalField('اعتبار مالی', max_digits=8, decimal_places=2, default=0)
    city = models.CharField('شهر', max_length=100)
    address = models.TextField('آدرس', max_length=250)

    def __str__(self):
        return self.user.get_full_name()
