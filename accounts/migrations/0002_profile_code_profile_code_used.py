# Generated by Django 4.2 on 2024-06-26 21:02

from django.db import migrations, models
import utils.code


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='code',
            field=models.CharField(default=utils.code.generaste_code, max_length=8, verbose_name='Code'),
        ),
        migrations.AddField(
            model_name='profile',
            name='code_used',
            field=models.BooleanField(default=False, verbose_name='Code Used'),
        ),
    ]
