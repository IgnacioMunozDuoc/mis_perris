# Generated by Django 2.1.2 on 2018-11-20 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181027_2224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='persona',
            options={'verbose_name': 'Persona Agregada', 'verbose_name_plural': 'Persona Agregada '},
        ),
        migrations.AlterField(
            model_name='persona',
            name='run',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=9),
        ),
    ]
