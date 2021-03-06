# Generated by Django 3.1.3 on 2020-11-05 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_classtag_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='url',
            new_name='channel_url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='product',
            name='subtitle_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='chapter',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='chapter_detail',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
