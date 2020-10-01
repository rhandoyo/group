# Generated by Django 2.0 on 2020-06-26 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('detail', models.TextField()),
                ('gambar', models.ImageField(default='', upload_to='images/')),
            ],
        ),
    ]
