# Generated by Django 2.1.1 on 2018-09-08 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identify', '0002_auto_20180905_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='faceEncode',
            field=models.FileField(upload_to=''),
        ),
    ]
