# Generated by Django 3.0 on 2020-01-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='opg_name',
            field=models.CharField(default='OPG', max_length=64, null=True),
        ),
    ]
