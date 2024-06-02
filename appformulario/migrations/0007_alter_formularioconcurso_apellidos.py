# Generated by Django 5.0.6 on 2024-05-12 19:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appformulario', '0006_alter_formularioconcurso_apellidos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioconcurso',
            name='apellidos',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Apellido Invalido', regex='^[a-zA-ZñÑ ]*$')]),
        ),
    ]