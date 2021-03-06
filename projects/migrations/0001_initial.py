# Generated by Django 3.2.9 on 2021-11-25 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('discription', models.TextField(max_length=50, null=True)),
                ('admin', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=100)),
                ('pending_tasks', models.TextField(max_length=120)),
                ('working_tasks', models.TextField(max_length=120)),
                ('completed_tasks', models.TextField(max_length=120)),
            ],
        ),
    ]
