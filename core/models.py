from django.db import models
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
    title = models.CharField('Название', max_length=128, unique=True)
    number_of_tables = models.PositiveSmallIntegerField('Количество столов')
    logo = models.ImageField('Логотип')
    guests = models.ManyToManyField(Guest, through='GuestFoodEstablishmentM2M', related_name='food_establishments')

    def __str__(self):
        return self.title


class GuestFoodEstablishmentM2M(models.Model):
    """
    Many-to-many for guests and food establishments
    """
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    food_establishment = models.ForeignKey(FoodEstablishment, on_delete=models.CASCADE)
    member_since = models.DateField('Первое посещение')
    number_of_visits = models.PositiveSmallIntegerField('Количество посещений')

    class Meta:
        unique_together = ['guest', 'food_establishment']

    def __str__(self):
        return self.food_establishment + '-' + self.guest


class Reservation(models.Model):
    """
    Model for reservations
    """
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='reservations')
    food_establishment = models.ForeignKey(FoodEstablishment, on_delete=models.CASCADE, related_name='reservations')
    start_date = models.DateTimeField('Дата и время начала брони')
    end_date = models.DateTimeField('Дата и время окончания брони')


class Table(models.Model):
    """
    Model for tables
    """
    number = models.PositiveSmallIntegerField('Номер стола')
    number_of_seats = models.PositiveSmallIntegerField('Количество мест за столом')
    smoke = models.BooleanField('Стол для курящих')


class ReservedTable(models.Model):
    """
    Model for tables on each reseration
    """
    table = models.OneToOneField(Table, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)