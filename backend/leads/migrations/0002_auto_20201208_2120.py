# Generated by Django 3.1.3 on 2020-12-08 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='median_salary',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='technology',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='contact_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='WebLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.CharField(max_length=100)),
                ('job_lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='leads.lead')),
            ],
        ),
    ]
