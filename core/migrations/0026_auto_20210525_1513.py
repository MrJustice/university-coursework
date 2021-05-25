# Generated by Django 3.1.7 on 2021-05-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20210524_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodestablishment',
            name='cousine',
            field=models.CharField(choices=[('BY', 'Национальная'), ('RU', 'Русская'), ('FR', 'Французская'), ('I', 'Итальянская'), ('CN', 'Китайская'), ('KR', 'Корейская'), ('PA', 'Паназиатская'), ('EU', 'Европейская')], default='BY', max_length=2, verbose_name='Кухня'),
        ),
    ]