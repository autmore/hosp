from random import choice

from django.contrib.auth.models import AbstractUser, User
from django.db import models


# 0 - patient
# 1 - doctor
# 2 - medsestra
# aibolit - GWiQZ3DvcnSWx8w
class CustomUser(AbstractUser):
    # Добавление собственного поля 'position'
    position = models.IntegerField(default=0, null=True, blank=True)

    # Переопределение строкового представления
    def __str__(self):
        return self.username

    # Для предотвращения ошибок с обратными связями, добавим related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Уникальное имя для обратной связи
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Уникальное имя для обратной связи
        blank=True
    )
    user_id = models.ManyToManyField(
        'auth.User',
        related_name='user',  # Уникальное имя для обратной связи
        blank=True
    )


class Diagnosis(models.Model):
    class DiagnosisName(models.TextChoices):
        FLU = 'flu', 'Грипп'
        PNEUMONIA = 'pneumonia', 'Пневмония'
        ALLERGY = 'allergy', 'Аллергия'
        COLD = 'cold', 'Простуда'

    class DiagnosisDescription(models.TextChoices):
        FLU_DESC = 'Грипп — острое респираторное заболевание.'
        PNEUMONIA_DESC = 'Пневмония — воспаление легких.'
        ALLERGY_DESC = 'Аллергия — реакция организма на внешние раздражители.'
        COLD_DESC = 'Простуда — общее недомогание, вызванное вирусом.'

    name = models.CharField(
        max_length=50,
        choices=DiagnosisName.choices,  # Список возможных значений для имени диагноза
        default=DiagnosisName.FLU,  # Значение по умолчанию для имени диагноза
    )
    description = models.CharField(
        max_length=255,
        choices=DiagnosisDescription.choices,  # Список возможных значений для описания диагноза
        default=DiagnosisDescription.FLU_DESC,  # Значение по умолчанию для описания диагноза
    )
    doctor = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='diagnoses')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Heal(models.Model):
    class Disease(models.TextChoices):
        FLU = 'flu', 'Грипп'
        PNEUMONIA = 'pneumonia', 'Пневмония'
        ALLERGY = 'allergy', 'Аллергия'
        COLD = 'cold', 'Простуда'

    class TreatmentDescription(models.TextChoices):
        FLU_TREATMENT = 'flu_treatment', 'Лечение гриппа: отдых, питье, жаропонижающие.'
        PNEUMONIA_TREATMENT = 'pneumonia_treatment', 'Лечение пневмонии: антибиотики, госпитализация.'
        ALLERGY_TREATMENT = 'allergy_treatment', 'Лечение аллергии: антигистамины, избегание аллергена.'
        COLD_TREATMENT = 'cold_treatment', 'Лечение простуды: теплые напитки, отдых, витамины.'

    disease = models.ManyToManyField('Diagnosis', related_name='customuser_set', blank=True)
    treatment = models.CharField(
        max_length=255,
        choices=TreatmentDescription.choices,  # Список возможных вариантов лечения
        default=TreatmentDescription.FLU_TREATMENT,  # Лечение по умолчанию (для гриппа)
    )
    doctor = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                               related_name='heals')  # Врач, назначивший лечение
    date_added = models.DateTimeField(auto_now_add=True)  # Дата назначения лечения

    def __str__(self):
        return f"Лечение для {self.disease} - {self.treatment}"


def __str__(self):
    return self.name
