# Generated by Django 4.0.3 on 2022-05-21 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_aabasoft'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
