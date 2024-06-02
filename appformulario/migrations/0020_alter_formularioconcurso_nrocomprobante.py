# Generated by Django 5.0.6 on 2024-05-14 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appformulario', '0019_alter_formularioconcurso_nrocomprobante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioconcurso',
            name='nrocomprobante',
            field=models.CharField(error_messages={'unique': 'Este numero de comprobante ya ha sido registrado.'}, max_length=15, unique=True),
        ),
    ]