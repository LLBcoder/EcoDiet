# Generated by Django 3.1.5 on 2021-03-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplan', '0016_auto_20210307_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='ingredient',
            field=models.CharField(choices=[('None', 'None'), ('Tomato', 'tomato'), ('Mushrooms', 'mushrooms'), ('Olives', 'olives')], max_length=30),
        ),
        migrations.AlterField(
            model_name='intolerances',
            name='intolerance',
            field=models.CharField(choices=[('None', 'None'), ('Dairy', 'Dairy'), ('Egg', 'Egg'), ('Gluten', 'Gluten'), ('Grain', 'Grain'), ('Peanut', 'Peanut'), ('Seafood', 'Seafood'), ('Sesame', 'Sesame'), ('Shellfish', 'Shellfish'), ('Soy', 'Soy'), ('Sulfite', 'Sulfite'), ('Tree Nut', 'Tree Nut'), ('Wheat', 'Wheat')], max_length=30),
        ),
    ]
