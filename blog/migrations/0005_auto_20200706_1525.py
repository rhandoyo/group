# Generated by Django 2.0 on 2020-07-06 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200706_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermasuk',
            old_name='user_masuk',
            new_name='nama_user_masuk',
        ),
    ]