# Generated by Django 2.0 on 2020-07-07 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200706_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='waktu_posting',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
