# Generated by Django 3.2.10 on 2024-01-29 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logindb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('e_mail', models.EmailField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]