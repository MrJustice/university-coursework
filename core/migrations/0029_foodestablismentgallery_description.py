# Generated by Django 3.1.7 on 2021-05-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20210525_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodestablismentgallery',
            name='description',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
