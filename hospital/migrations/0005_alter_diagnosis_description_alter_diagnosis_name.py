# Generated by Django 5.1.4 on 2024-12-12 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_alter_diagnosis_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='description',
            field=models.CharField(choices=[('Грипп — острое респираторное заболевание.', 'Flu Desc'), ('Пневмония — воспаление легких.', 'Pneumonia Desc'), ('Аллергия — реакция организма на внешние раздражители.', 'Allergy Desc'), ('Простуда — общее недомогание, вызванное вирусом.', 'Cold Desc')], default='Грипп — острое респираторное заболевание.', max_length=255),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='name',
            field=models.CharField(choices=[('flu', 'Грипп'), ('pneumonia', 'Пневмония'), ('allergy', 'Аллергия'), ('cold', 'Простуда')], default='flu', max_length=50),
        ),
    ]
