# Generated by Django 3.1.7 on 2021-03-10 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodestablishment',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='food_establishment', to=settings.AUTH_USER_MODEL),
        ),
    ]
