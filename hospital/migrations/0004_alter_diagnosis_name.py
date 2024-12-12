# Generated by Django 5.1.4 on 2024-12-12 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_diagnosis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='name',
            field=models.CharField(choices=[('flu', 'Грипп'), ('pneumonia', 'Пневмония'), ('allergy', 'Аллергия'), ('cold', 'Простуда')], default='cold', max_length=50),
        ),
    ]
