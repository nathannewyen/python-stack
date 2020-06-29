# Generated by Django 2.2.4 on 2020-05-03 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard_app', '0009_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_message_id', to='user_dashboard_app.Message')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user_id', to='user_dashboard_app.User')),
            ],
        ),
    ]