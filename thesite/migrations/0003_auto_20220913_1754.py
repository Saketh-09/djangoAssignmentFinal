# Generated by Django 3.2.15 on 2022-09-13 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesite', '0002_auto_20220913_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='id',
            new_name='detailsId',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='userID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]