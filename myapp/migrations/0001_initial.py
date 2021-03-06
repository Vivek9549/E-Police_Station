# Generated by Django 4.0.2 on 2022-04-08 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40)),
                ('lname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('pic', models.FileField(default='berlin_1.jpg', upload_to='Profile')),
            ],
        ),
        migrations.CreateModel(
            name='FIR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('idate', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=6)),
                ('address', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=50)),
                ('charge', models.CharField(max_length=100)),
                ('victim', models.CharField(blank=True, max_length=10, null=True)),
                ('ifname', models.CharField(max_length=50)),
                ('ilname', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('iid', models.FileField(blank=True, null=True, upload_to='Informant ID')),
                ('iaddress', models.CharField(max_length=100)),
                ('evi', models.FileField(blank=True, null=True, upload_to='Evidence')),
                ('sfname', models.CharField(blank=True, max_length=50, null=True)),
                ('slname', models.CharField(blank=True, max_length=50, null=True)),
                ('sdetail', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('invest', models.BooleanField(default=False)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
                ('police', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.station')),
            ],
        ),
    ]
