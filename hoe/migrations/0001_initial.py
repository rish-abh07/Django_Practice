# Generated by Django 4.0.3 on 2022-03-21 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('email', models.CharField(max_length=130)),
                ('suggestion', models.CharField(max_length=300)),
            ],
        ),
    ]
