# Generated by Django 4.1.4 on 2022-12-16 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_hitmen_status_mission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hitmen',
            name='assigned_manager',
            field=models.ForeignKey(blank=True, help_text='Manager assigned for this hitmen', on_delete=django.db.models.deletion.CASCADE, to='users.manager'),
        ),
    ]