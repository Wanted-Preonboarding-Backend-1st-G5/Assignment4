# Generated by Django 3.2.9 on 2021-11-13 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211112_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradelog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]