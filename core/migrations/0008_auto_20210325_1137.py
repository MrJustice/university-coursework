# Generated by Django 3.1.7 on 2021-03-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_foodestablishment_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('rating', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Рейтинг')),
            ],
        ),
        migrations.AddField(
            model_name='foodestablishment',
            name='preview_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Превью'),
        ),
        migrations.AddField(
            model_name='foodestablishment',
            name='type',
            field=models.CharField(choices=[('B', 'Бар'), ('C', 'Кафе'), ('R', 'Ресторан')], default='C', max_length=1, verbose_name='Тип заведения'),
        ),
        migrations.AlterField(
            model_name='foodestablishment',
            name='cousine',
            field=models.CharField(choices=[('BY', 'Национальная'), ('RU', 'Русская'), ('FR', 'Французская'), ('I', 'Итальянская'), ('CN', 'Китайская'), ('KR', 'Корейская')], default='BY', max_length=2, verbose_name='Кухня'),
        ),
        migrations.AlterField(
            model_name='foodestablishment',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Рейтинг'),
        ),
    ]
