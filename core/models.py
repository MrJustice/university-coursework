from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

BLANK_NULL = {'blank': True, 'null': True}


class Guest(models.Model):
    """
    Model for guests
    """
    first_name = models.CharField('Имя', max_length=128)
    phone = PhoneNumberField('Номер телефона', unique=True, **BLANK_NULL)

    def __str__(self):
        return self.first_name


class FoodEstablishment(models.Model):
    """
    Model for food establishments
    """
    BELARUS = 'BY'
    RUSSIA = 'RU'
    FRANCE = 'FR'
    ITALY = 'I'
    CHINA = 'CN'
    KOREA = 'KR'

    COUSINE_CHOICES = [
        (BELARUS, 'Национальная'),
        (RUSSIA, 'Русская'),
        (FRANCE, 'Французская'),
        (ITALY, 'Итальянская'),
        (CHINA, 'Китайская'),
        (KOREA, 'Корейская')
    ]

    BAR = 'B'
    CAFE = 'C'
    RESTAURANT = 'R'

    TYPE_CHOICES = [
        (BAR, 'Бар'),
        (CAFE, 'Кафе'),
        (RESTAURANT, 'Ресторан')
    ]

    owner = models.ForeignKey(User, related_name='food_establishments', on_delete=models.PROTECT)
    title = models.CharField('Название', max_length=128, unique=True)
    description = models.CharField('Описание', max_length=1000, **BLANK_NULL)
    type = models.CharField('Тип заведения', max_length=1, choices=TYPE_CHOICES, default=TYPE_CHOICES[1][0])
    cousine = models.CharField('Кухня', max_length=2, choices=COUSINE_CHOICES, default=COUSINE_CHOICES[0][0])
    average_check = models.PositiveSmallIntegerField('Средний чек', **BLANK_NULL)
    rating = models.DecimalField('Рейтинг', max_digits=2, decimal_places=1, default=0.0, **BLANK_NULL)
    phone = PhoneNumberField('Номер телефона', **BLANK_NULL)
    location = models.CharField(max_length=128, blank=True)
    opening_time = models.CharField(max_length=5, blank=True)
    closing_time = models.CharField(max_length=5, blank=True)
    email = models.EmailField('Адрес электронной почты', max_length=128, **BLANK_NULL)
    big_image = models.ImageField('Логотип', **BLANK_NULL)
    preview_image = models.ImageField('Превью', **BLANK_NULL)
    guests = models.ManyToManyField(Guest, through='GuestFoodEstablishmentM2M', related_name='food_establishments')

    def __str__(self):
        return self.get_type_display() + ' "' + self.title + '"'

    @property
    def working_hours(self):
        return self.opening_time + ' - ' + self.closing_time

    @property
    def get_number_of_tables(self):
        return self.tables.all().count()


class Feedback(models.Model):
    """
    Отзывы
    """
    guest = models.ForeignKey(Guest, on_delete=models.SET_NULL, null=True)
    food_establishment = models.ForeignKey(FoodEstablishment, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=500, **BLANK_NULL)
    rating = models.PositiveSmallIntegerField('Рейтинг', **BLANK_NULL)


class GuestFoodEstablishmentM2M(models.Model):
    """
    Many-to-many for guests and food establishments
    """
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    food_establishment = models.ForeignKey(FoodEstablishment, on_delete=models.CASCADE)
    member_since = models.DateField('Первое посещение', **BLANK_NULL)
    number_of_visits = models.PositiveSmallIntegerField('Количество посещений', default=0, **BLANK_NULL)

    class Meta:
        unique_together = ['guest', 'food_establishment']

    def __str__(self):
        return str(self.food_establishment) + ' - Гость: ' + str(self.guest)

    def increment_number_of_visits(self):
        self.number_of_visits = self.number_of_visits + 1


class Table(models.Model):
    """
    Model for tables
    """
    food_establishment = models.ForeignKey(FoodEstablishment, related_name='tables', on_delete=models.CASCADE, null=True)
    number = models.PositiveSmallIntegerField('Номер стола')
    smoke = models.BooleanField('Стол для курящих', default=False)
    image = models.ImageField('Фото', **BLANK_NULL)

    def __str__(self):
        return f'Столик номер {self.number}'


class Reservation(models.Model):
    """
    Model for reservations
    """
    guest_food_establishment = models.ForeignKey(GuestFoodEstablishmentM2M, on_delete=models.CASCADE)
    number_of_persons = models.PositiveSmallIntegerField('Количество персон', **BLANK_NULL)
    start_date = models.DateTimeField('Дата и время начала брони')
    table = models.PositiveSmallIntegerField('Номер стола', **BLANK_NULL)

    def __str__(self):
        return str(self.guest_food_establishment) + ' в ' + self.start_date.strftime('%H:%M')


# class ReservedTable(models.Model):
#     """
#     Model for tables on each reservation
#     """
#     table = models.OneToOneField(Table, on_delete=models.CASCADE)
#     reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)