from django.db import models


class Cursus(models.Model):
    name = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        default='aucun'
    )
    year_from_bac = models.SmallIntegerField(
        help_text='year since the bac',
        verbose_name='year',
        blank=False,
        default=0
    )
    scholar_year = models.CharField(
        max_length=9,
        blank=False,
        null=True,
        default='0000-0001'
    )

    def __str__(self):
        return '{}-{}'.format(self.name, self.scholar_year)


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    birth_date = models.DateField(
        verbose_name='date of birth',
        blank=False,
        null=False
    )
    last_name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        help_text='last name of student',
        default='???'
    )
    phone = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        help_text='phone number of student',
        default='099999999'
    )
    mail = models.CharField(
        max_length=255,
        verbose_name='email of student',
        blank=False,
        null=False,
        help_text='email of student',
        default='x@y.z'
    )
    comment = models.CharField(
        max_length=50,
        blank=True,
        null=False,
        help_text='comment on student',
        default=''
    )
    cursus = models.ForeignKey(
        Cursus,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return '{}/{}/{}'.format(self.first_name, self.last_name, self.id)


class Presence(models.Model):
    date = models.DateField(
        verbose_name='Date of roll',
        blank=False,
        null=False
    )

    reason = models.CharField(
        max_length=50,
        blank=True,
        null=False,
        help_text='Reason of absence',
        default=''
    )

    isMissing = models.BooleanField()

    student = models.ForeignKey(
        Student,
        null=False,
        on_delete=models.CASCADE
    )
