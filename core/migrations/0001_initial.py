# Generated by Django 3.1.7 on 2021-03-10 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodEstablishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='Название')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Номер телефона')),
                ('location', models.CharField(blank=True, max_length=128)),
                ('email', models.EmailField(blank=True, max_length=128, null=True, verbose_name='Адрес электронной почты')),
                ('number_of_tables', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество столов')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Логотип')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=128, verbose_name='Фамилия')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='GuestFoodEstablishmentM2M',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_since', models.DateField(blank=True, null=True, verbose_name='Первое посещение')),
                ('number_of_visits', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество посещений')),
                ('food_establishment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.foodestablishment')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.guest')),
            ],
            options={
                'unique_together': {('guest', 'food_establishment')},
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_persons', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество персон')),
                ('start_date', models.DateTimeField(verbose_name='Дата и время начала брони')),
                ('end_date', models.DateTimeField(verbose_name='Дата и время окончания брони')),
                ('guest_food_establishment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.guestfoodestablishmentm2m')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Номер стола')),
                ('number_of_seats', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество мест за столом')),
                ('smoke', models.BooleanField(default=False, verbose_name='Стол для курящих')),
                ('status', models.CharField(choices=[('FR', 'Free'), ('BKD', 'Booked')], default='FR', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ReservedTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.reservation')),
                ('table', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.table')),
            ],
        ),
        migrations.AddField(
            model_name='foodestablishment',
            name='guests',
            field=models.ManyToManyField(related_name='food_establishments', through='core.GuestFoodEstablishmentM2M', to='core.Guest'),
        ),
        migrations.AddField(
            model_name='foodestablishment',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
