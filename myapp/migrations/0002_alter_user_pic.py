# Generated by Django 4.0.2 on 2022-04-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=models.FileField(default='default.jpg', upload_to='Profile'),
        ),
    ]
