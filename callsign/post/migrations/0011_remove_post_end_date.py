# Generated by Django 4.0.3 on 2022-10-04 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_post_end_date_alter_post_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='end_date',
        ),
    ]
