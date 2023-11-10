# Generated by Django 4.2.6 on 2023-11-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0009_club'),
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='club',
            name='page',
            field=models.CharField(choices=[('1', 'Language'), ('2', 'Debate'), ('3', 'ICT'), ('4', 'Chess'), ('5', 'Math'), ('6', 'Science')], default='SELECT', max_length=255),
        ),
    ]
