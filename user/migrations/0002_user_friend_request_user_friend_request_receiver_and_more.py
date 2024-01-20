# Generated by Django 5.0.1 on 2024-01-20 17:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("friend_request", "0002_initial"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="friend_request",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users_friend_request",
                to="friend_request.friendrequest",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="friend_request_receiver",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users_friend_request_receiver",
                to="friend_request.friendrequest",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
