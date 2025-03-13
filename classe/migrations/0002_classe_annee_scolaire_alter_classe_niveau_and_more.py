# Generated by Django 5.1.6 on 2025-03-07 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe',
            name='annee_scolaire',
            field=models.CharField(default='2025', max_length=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classe',
            name='niveau',
            field=models.CharField(choices=[('primaire', 'Primaire'), ('college', 'Collège'), ('lycee', 'Lycée')], max_length=50),
        ),
        migrations.AlterField(
            model_name='classe',
            name='nom',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
