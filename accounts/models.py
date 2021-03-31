from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.choices import gender_choice


class Profile(models.Model):
    class Meta:
        verbose_name = 'پروفایل کاربران'
        verbose_name_plural = 'پروفایل کاربران'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='حساب')
    avatar = models.ImageField('آواتار', upload_to='accounts_avatar/', null=True, blank=True)
    phone = models.CharField('تلفن همراه', null=False, max_length=20)

    gender = models.IntegerField('جنسیت', choices=gender_choice, blank=True, null=True)
    birthday = models.DateField('تاریخ تولد', null=True, blank=True)
    credit_money = models.IntegerField('اعتبار مالی', default=0)
    city = models.CharField('شهر', max_length=100, default='تبریز')
    address = models.TextField('آدرس', max_length=250, default='ایران')

    def __str__(self):
        return self.user.get_full_name()

    def buy(self, total_price):
        if self.credit_money < total_price:
            return False
        else:
            self.credit_money -= total_price
            self.save()
            return True

    # behaviors
    def increase_credit(self, amount):
        self.credit_money += amount
        self.save()


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Payment(models.Model):
    class Meta:
        verbose_name = 'پرداخت'
        verbose_name_plural = 'پرداخت'

    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, verbose_name='کاربر')
    amount = models.PositiveIntegerField('مبلغ')
    transaction_time = models.DateTimeField('زمان تراکنش', auto_now_add=True)
    transaction_code = models.CharField('شماره تراکنش', max_length=30)
