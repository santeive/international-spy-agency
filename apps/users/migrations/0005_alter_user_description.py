# Generated by Django 4.1.4 on 2022-12-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_hitmen_assigned_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.CharField(blank=True, help_text='Brief description for this position', max_length=80, null=True),
        ),
    ]