# Generated by Django 4.0.3 on 2022-12-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_image',
            field=models.CharField(default='https://cdn5.vectorstock.com/i/1000x1000/62/39/coming-soon-nature-concept-vector-4896239.jpg', max_length=500),
        ),
    ]
