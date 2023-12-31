# Generated by Django 4.2.6 on 2023-10-20 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('NAME', models.CharField(max_length=255)),
                ('DATE', models.DateField()),
                ('DUE', models.DateField()),
                ('FEE', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CONTACT_NO', models.CharField(max_length=20)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('STATUS', models.CharField(max_length=50)),
            ],
        ),
    ]
