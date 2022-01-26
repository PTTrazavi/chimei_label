# Generated by Django 2.2.4 on 2022-01-24 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('ref', models.ImageField(upload_to='images/')),
                ('ap', models.ImageField(upload_to='images/')),
                ('apl', models.CharField(max_length=32, null=True)),
                ('lat', models.ImageField(upload_to='images/')),
                ('latl', models.CharField(max_length=32, null=True)),
                ('date_of_update', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
