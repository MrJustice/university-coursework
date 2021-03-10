from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

BLANK_NULL = {'blank': True, 'null': True}


class Guest(models.Model):
    """
    Model for guests
    """
    first_name = models.CharField('Имя', max_length=128)
    last_name = models.CharField('Фамилия', max_length=128, blank=True)
    phone = PhoneNumberField('Номер телефона', **BLANK_NULL)

    def __str__(self):
        return self.last_name + ' ' + self.first_name


class FoodEstablishment(models.Model):
    """
    Model for food establishments
    """
    owner = models.OneToOneField(User, related_name='food_establishment', on_delete=models.PROTECT)
    title = models.CharField('Название', max_length=128, unique=True)
    phone = PhoneNumberField('Номер телефона', **BLANK_NULL)
    location = models.CharField(max_length=128, blank=True)
    email = models.EmailField('Адрес электронной почты', max_length=128, **BLANK_NULL)
    number_of_tables = models.PositiveSmallIntegerField('Количество столов', **BLANK_NULL)
    logo = models.ImageField('Логотип', **BLANK_NULL)
    guests = models.ManyToManyField(Guest, through='GuestFoodEstablishmentM2M', related_name='food_establishments')

    def __str__(self):
        return self.title


class GuestFoodEstablishmentM2M(models.Model):
    """
    Many-to-many for guests and food establishments
    """
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    food_establishment = models.ForeignKey(FoodEstablishment, on_delete=models.CASCADE)
    member_since = models.DateField('Первое посещение', **BLANK_NULL)
    number_of_visits = models.PositiveSmallIntegerField('Количество посещений', **BLANK_NULL)

    class Meta:
        unique_together = ['guest', 'food_establishment']

    def __str__(self):
        return self.food_establishment + '-' + self.guest


class Reservation(models.Model):
    """
    Model for reservations
    """
    guest_food_establishment = models.ForeignKey(GuestFoodEstablishmentM2M, on_delete=models.CASCADE)
    number_of_persons = models.PositiveSmallIntegerField('Количество персон', **BLANK_NULL)
    start_date = models.DateTimeField('Дата и время начала брони')
    end_date = models.DateTimeField('Дата и время окончания брони')

    def __str__(self):
        return str(self.guest_food_establishment) + ': ' + self.start_date


class Table(models.Model):
    """
    Model for tables
    """
    FREE = 'FR'
    BOOKED = 'BKD'
    STATUS_CHOICES = [
        (FREE, 'Free'),
        (BOOKED, 'Booked')
    ]
    number = models.PositiveSmallIntegerField('Номер стола')
    number_of_seats = models.PositiveSmallIntegerField('Количество мест за столом', **BLANK_NULL)
    smoke = models.BooleanField('Стол для курящих', default=False)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=FREE)


class ReservedTable(models.Model):
    """
    Model for tables on each reservation
    """
    table = models.OneToOneField(Table, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)