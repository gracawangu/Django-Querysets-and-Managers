# Generated by Django 4.0.6 on 2022-07-18 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_alter_link_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]