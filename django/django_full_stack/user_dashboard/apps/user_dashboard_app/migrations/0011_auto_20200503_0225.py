# Generated by Django 2.2.4 on 2020-05-03 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard_app', '0010_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user_comment',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='user_id',
            new_name='user_message',
        ),
    ]
