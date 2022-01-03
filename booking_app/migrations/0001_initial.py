# Generated by Django 3.2.9 on 2021-12-30 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('device', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=200)),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hiuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]