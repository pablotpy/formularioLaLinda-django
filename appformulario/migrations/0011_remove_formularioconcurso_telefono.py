# Generated by Django 5.0.6 on 2024-05-13 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appformulario', '0010_alter_formularioconcurso_nrocomprobante_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formularioconcurso',
            name='telefono',
        ),
    ]