# Generated by Django 3.1.5 on 2021-03-06 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplan', '0003_auto_20210306_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='ingredient',
            field=models.CharField(choices=[('Tomato', 'tomato'), ('Mushrooms', 'mushrooms'), ('Olives', 'olives')], max_length=30),
        ),
    ]
