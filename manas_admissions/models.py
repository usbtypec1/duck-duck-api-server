from django.db import models

from users.models import User

__all__ = ('Department', 'Application', 'Applicant')


class Department(models.Model):
    class MainScoreType(models.IntegerChoices):
        NATURAL_SCIENCES = 1
        HUMANITARIAN_SCIENCES = 2
        GENERAL_SCIENCES = 3

    name = models.CharField(max_length=255)
    main_score_type = models.PositiveSmallIntegerField(
        choices=MainScoreType.choices,
    )


class Application(models.Model):
    class Stage(models.IntegerChoices):
        FIRST = 1
        SECOND = 2
        THIRD = 3

    number = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    main_score = models.FloatField()
    ort_score = models.PositiveSmallIntegerField(null=True, blank=True)
    english_score = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField()
    stage = models.PositiveSmallIntegerField(choices=Stage.choices)

    class Meta:
        unique_together = ('number', 'stage')


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=8)
    application = models.ForeignKey(
        Application,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    natural_sciences_score = models.FloatField()
    humanitarian_sciences_score = models.FloatField()
    general_sciences_score = models.FloatField()
    ort_score = models.PositiveSmallIntegerField(null=True, blank=True)
    english_score = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'number')
