# Generated by Django 4.2.6 on 2023-10-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='noticetbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_id', models.IntegerField()),
                ('notice_title', models.CharField(max_length=255)),
                ('notice_des', models.TextField()),
                ('notice_date', models.CharField(max_length=255)),
            ],
        ),
    ]