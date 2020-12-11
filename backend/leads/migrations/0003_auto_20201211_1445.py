# Generated by Django 3.1.3 on 2020-12-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20201208_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='technology',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='weblink',
            name='uri',
            field=models.CharField(max_length=300),
        ),
    ]