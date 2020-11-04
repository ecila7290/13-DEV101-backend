# Generated by Django 3.1.3 on 2020-11-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20201104_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='introduction',
            old_name='Product',
            new_name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='chapter',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='chapter_detail',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='subtitle',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]