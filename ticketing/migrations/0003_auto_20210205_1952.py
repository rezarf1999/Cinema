# Generated by Django 3.1.4 on 2021-02-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0002_auto_20210125_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Cinema_Images/', verbose_name='عکس'),
        ),
    ]