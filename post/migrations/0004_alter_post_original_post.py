# Generated by Django 5.0.1 on 2024-01-23 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='original_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='original_post_shared_post_rel', to='post.post'),
        ),
    ]
