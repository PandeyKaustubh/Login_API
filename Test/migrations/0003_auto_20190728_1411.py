# Generated by Django 2.2.3 on 2019-07-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_auto_20190727_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudo',
            name='Fa_Mobile_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sudo',
            name='Mobile_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='Password',
            field=models.CharField(max_length=100),
        ),
    ]
