# Generated by Django 4.0.2 on 2022-04-12 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_fir_invest'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='img',
            field=models.FileField(default='police station.jpg', upload_to='Station'),
        ),
    ]
