# Generated by Django 3.1.7 on 2021-03-16 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210310_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='food_establishment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.foodestablishment'),
        ),
    ]