# Generated by Django 2.1.1 on 2018-09-02 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plays', '0002_auto_20180902_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='title',
            field=models.CharField(blank=True, choices=[('KI', 'King'), ('QU', 'Queen'), ('DU', 'Duke'), ('CO', 'Count')], max_length=2, null=True),
        ),
    ]