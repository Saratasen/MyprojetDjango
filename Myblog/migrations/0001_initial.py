# Generated by Django 3.2.18 on 2023-06-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('resume', models.TextField()),
                ('miniature', models.ImageField(upload_to='miniatures/')),
                ('contenu', models.TextField()),
                ('auteur', models.CharField(max_length=100)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
