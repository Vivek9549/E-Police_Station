# Generated by Django 4.0.2 on 2022-04-24 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_complaint_date_alter_complaint_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fir',
            name='sdetail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
