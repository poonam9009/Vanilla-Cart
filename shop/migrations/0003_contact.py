# Generated by Django 2.2.7 on 2020-01-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200123_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=400)),
                ('desc', models.CharField(default=' ', max_length=400)),
            ],
        ),
    ]
