# Generated by Django 3.1.4 on 2021-03-26 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210325_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='accounts_avatar/', verbose_name='آواتار'),
        ),
    ]