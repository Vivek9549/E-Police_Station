# Generated by Django 4.0.2 on 2022-04-29 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_missing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missing',
            name='pic',
            field=models.FileField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
