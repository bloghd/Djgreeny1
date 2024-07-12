# Generated by Django 4.2 on 2024-07-01 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('logo', models.ImageField(upload_to='company/', verbose_name='Logo')),
                ('about', models.TextField(max_length=500, verbose_name='About')),
                ('fa_link', models.URLField(verbose_name='Facebook')),
                ('tw_link', models.URLField(verbose_name='Tweiter')),
                ('ins_link', models.URLField(verbose_name='Instgarm')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Phone Number')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
    ]