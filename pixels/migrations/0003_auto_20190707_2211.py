# Generated by Django 2.2.3 on 2019-07-07 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixels', '0002_requests_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='client',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requests',
            name='device',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requests',
            name='os',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]