# Generated by Django 4.0.5 on 2022-06-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('address', models.CharField(max_length=200)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
