# Generated by Django 3.2.23 on 2023-11-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='establishedDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entity',
            name='licenceNo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entity',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
