# Generated by Django 4.1.1 on 2022-09-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MylinebotApp', '0002_user_info_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='ASML',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_info',
            name='CTBC',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_info',
            name='Cathay',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_info',
            name='Chunghwa',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_info',
            name='Kronos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_info',
            name='Line',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_info',
            name='NXP',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_info',
            name='Pixart',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_info',
            name='STM',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_info',
            name='Yahoo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_info',
            name='a104',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_info',
            name='tsmc',
            field=models.IntegerField(default=0),
        ),
    ]
