# Generated by Django 5.0.6 on 2024-05-13 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appformulario', '0012_formularioconcurso_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioconcurso',
            name='nrocomprobante',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='formularioconcurso',
            name='telefono',
            field=models.CharField(max_length=12),
        ),
    ]
