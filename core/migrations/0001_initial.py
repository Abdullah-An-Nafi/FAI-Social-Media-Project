# Generated by Django 4.0.5 on 2022-07-28 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empinsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=12)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
    ]
