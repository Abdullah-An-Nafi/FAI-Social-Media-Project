# Generated by Django 4.0.5 on 2022-08-18 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_likespost_like_alter_likespost_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profileimg',
            field=models.ImageField(default='profilepic.jpg', upload_to='profile_images'),
        ),
    ]