# Generated by Django 4.1.4 on 2022-12-15 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_alter_childmodels_children_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childmodels',
            name='children_status',
            field=models.CharField(default='pending', help_text='children_status', max_length=50),
        ),
    ]
