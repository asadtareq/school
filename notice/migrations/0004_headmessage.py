# Generated by Django 4.2.6 on 2023-11-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0003_alter_notice_notice_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='headmessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('message', models.TextField()),
            ],
        ),
    ]