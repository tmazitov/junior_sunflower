# Generated by Django 5.1.2 on 2024-11-15 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_companyvacancy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyvacancy',
            name='company_id',
            field=models.IntegerField(),
        ),
    ]
