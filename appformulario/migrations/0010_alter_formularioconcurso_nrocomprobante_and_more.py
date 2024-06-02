# Generated by Django 5.0.6 on 2024-05-13 00:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appformulario', '0009_alter_formularioconcurso_nombres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioconcurso',
            name='nrocomprobante',
            field=models.IntegerField(validators=[django.core.validators.MaxLengthValidator(13)]),
        ),
        migrations.AlterField(
            model_name='formularioconcurso',
            name='telefono',
            field=models.IntegerField(validators=[django.core.validators.MaxLengthValidator(10)]),
        ),
    ]
