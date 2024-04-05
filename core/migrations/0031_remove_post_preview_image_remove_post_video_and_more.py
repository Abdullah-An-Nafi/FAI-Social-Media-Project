# Generated by Django 4.2.5 on 2023-10-20 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_post_preview_image_post_video_alter_post_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='preview_image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(upload_to='Post_image/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(default='user', max_length=30),
        ),
    ]