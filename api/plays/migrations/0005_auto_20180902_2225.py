# Generated by Django 2.1.1 on 2018-09-02 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plays', '0004_remove_line_play_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scene',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plays.Place'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='setting_text',
            field=models.TextField(blank=True),
        ),
    ]
